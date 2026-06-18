#!/usr/bin/env python3
r"""
InputToOutputMachine.py
========================
Converts every PDF in ./input into:
  - a Markdown file in ./output - mds   (<name>.md)
  - a dark, Obsidian-style HTML file in ./output - html  (<name>.html)

Design goals:
  - NEVER crash the whole batch because of one bad PDF or one bad page.
  - NEVER silently skip a page. If a page fails, it's clearly marked
    in the output instead of vanishing.
  - Extract real structure: headings (best-effort, from font size),
    paragraphs, tables (as proper Markdown/HTML tables), and embedded
    images (saved to disk + linked/embedded).
  - Produce a clean Obsidian-like dark theme HTML render of the Markdown.

Usage:
    python InputToOutputMachine.py
    (run it from the folder that contains input / output - mds / output - html,
     OR pass a base directory: python InputToOutputMachine.py "C:\path\to\MadGodsDisease")

Dependencies (install once):
    pip install pymupdf pdfplumber markdown
    pip install pikepdf   (optional, enables auto-decrypt of password-protected PDFs)
"""

import sys
import os
import re
import io
import shutil
import traceback
import datetime
import html as html_lib
from pathlib import Path

# ---- Third-party deps -------------------------------------------------
try:
    import fitz  # PyMuPDF -- best for image extraction + font-size heading detection
except ImportError:
    print("Missing dependency 'pymupdf'. Install with: pip install pymupdf")
    sys.exit(1)

try:
    import pdfplumber  # best for clean text + table extraction
except ImportError:
    print("Missing dependency 'pdfplumber'. Install with: pip install pdfplumber")
    sys.exit(1)

try:
    import markdown as md_lib  # to render markdown -> html body
except ImportError:
    print("Missing dependency 'markdown'. Install with: pip install markdown")
    sys.exit(1)

# pikepdf is optional but strongly recommended: lets us auto-decrypt PDFs that
# are "encrypted" with an empty/blank owner password (extremely common for
# downloaded textbooks/scanned docs) and repair some malformed PDFs via qpdf.
try:
    import pikepdf
    HAVE_PIKEPDF = True
except ImportError:
    HAVE_PIKEPDF = False


# =========================================================================
# CONFIG
# =========================================================================

INPUT_DIRNAME = "input"
OUTPUT_MD_DIRNAME = "output - mds"
OUTPUT_HTML_DIRNAME = "output - html"
IMAGES_SUBDIRNAME = "_images"   # created inside output-mds/<pdfname>_images/

MIN_IMAGE_DIMENSION = 20        # skip tiny junk images (tracking pixels, hairline dividers) by width/height in px
LOG_FILENAME = "_conversion_log.txt"


# =========================================================================
# LOGGING
# =========================================================================

class Logger:
    """Tees print() to console and to a log file, and tracks a summary table."""

    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.lines = []
        self.summary = []  # list of dicts per pdf

    def log(self, msg: str):
        print(msg)
        self.lines.append(msg)

    def write(self):
        try:
            self.log_path.write_text("\n".join(self.lines), encoding="utf-8")
        except Exception as e:
            print(f"  (could not write log file: {e})")

    def add_summary(self, filename, status, pages_ok, pages_failed, n_tables, n_images, note=""):
        self.summary.append({
            "filename": filename,
            "status": status,
            "pages_ok": pages_ok,
            "pages_failed": pages_failed,
            "n_tables": n_tables,
            "n_images": n_images,
            "note": note,
        })

    def print_summary(self):
        self.log("\n" + "=" * 78)
        self.log("SUMMARY")
        self.log("=" * 78)
        for s in self.summary:
            self.log(
                f"  [{s['status']:^7}] {s['filename']:<45} "
                f"pages_ok={s['pages_ok']:<4} pages_failed={s['pages_failed']:<3} "
                f"tables={s['n_tables']:<3} images={s['n_images']:<3} {s['note']}"
            )
        ok = sum(1 for s in self.summary if s["status"] == "OK")
        warn = sum(1 for s in self.summary if s["status"] == "WARN")
        fail = sum(1 for s in self.summary if s["status"] == "FAIL")
        self.log("-" * 78)
        self.log(f"  Total PDFs: {len(self.summary)}  |  OK: {ok}  WARN: {warn}  FAIL: {fail}")
        self.log("=" * 78)


# =========================================================================
# MARKDOWN HELPERS
# =========================================================================

def escape_md_table_cell(text: str) -> str:
    """Escape pipe chars and collapse newlines so table cells don't break rendering."""
    if text is None:
        return ""
    text = str(text).replace("\n", " ").replace("\r", " ")
    text = text.replace("|", "\\|")
    return text.strip()


def table_to_markdown(table_rows) -> str:
    """Convert a list-of-lists table (from pdfplumber) into a GitHub-flavored Markdown table."""
    if not table_rows or len(table_rows) == 0:
        return ""

    # Normalize row lengths (ragged tables happen often with pdfplumber)
    max_cols = max(len(r) for r in table_rows if r is not None)
    norm_rows = []
    for r in table_rows:
        r = r or []
        r = list(r) + [""] * (max_cols - len(r))
        norm_rows.append(r)

    header = norm_rows[0]
    body = norm_rows[1:]

    lines = []
    lines.append("| " + " | ".join(escape_md_table_cell(c) for c in header) + " |")
    lines.append("| " + " | ".join(["---"] * max_cols) + " |")
    for row in body:
        lines.append("| " + " | ".join(escape_md_table_cell(c) for c in row) + " |")
    return "\n".join(lines)


def clean_text_block(text: str) -> str:
    """Light cleanup of extracted PDF text without destroying structure."""
    if not text:
        return ""
    # Fix hyphenated line-break words: "exam-\nple" -> "example"
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    # Collapse 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def guess_heading_level(font_size: float, body_size_estimate: float) -> int:
    """Very rough heuristic: bigger font relative to typical body text => higher-level heading."""
    if body_size_estimate <= 0:
        body_size_estimate = 10.0
    ratio = font_size / body_size_estimate
    if ratio >= 1.8:
        return 1
    elif ratio >= 1.5:
        return 2
    elif ratio >= 1.25:
        return 3
    return 0  # not a heading


# =========================================================================
# PRE-PROCESSING: decrypt / repair via pikepdf before main conversion
# =========================================================================

def prepare_openable_pdf(pdf_path: Path, tmp_dir: Path, logger: Logger):
    """
    Attempt to produce a path to a PDF that pdfplumber/fitz can open cleanly.

    - If the PDF opens fine as-is, returns the original path unchanged.
    - If it's encrypted with an empty/blank password (very common for
      "print/copy restricted" PDFs), decrypts it via pikepdf and writes a
      clean temp copy, returning that path instead.
    - If it's malformed in a way qpdf can repair, also writes a repaired
      temp copy.
    - If nothing works, returns the original path anyway (the normal
      per-file error handling in convert_pdf_to_markdown will catch and
      report the failure -- this function never raises).

    Returns: (path_to_use, note_string_or_None)
    """
    if not HAVE_PIKEPDF:
        return pdf_path, None

    try:
        # Quick check: can pikepdf open it normally?
        with pikepdf.open(str(pdf_path)) as _:
            return pdf_path, None
    except pikepdf.PasswordError:
        # Encrypted -- try the most common case: empty/blank password.
        try:
            with pikepdf.open(str(pdf_path), password="") as pdf:
                out_path = tmp_dir / f"{pdf_path.stem}__decrypted.pdf"
                pdf.save(str(out_path))
                return out_path, "auto-decrypted (blank password)"
        except Exception as e:
            logger.log(f"      [decrypt] could not auto-decrypt with blank password: {e}")
            return pdf_path, None
    except Exception as e:
        # Possibly malformed/corrupt in a way pikepdf can still salvage via qpdf's repair.
        try:
            with pikepdf.open(str(pdf_path), allow_overwriting_input=False) as pdf:
                out_path = tmp_dir / f"{pdf_path.stem}__repaired.pdf"
                pdf.save(str(out_path))
                return out_path, "auto-repaired malformed structure"
        except Exception:
            # Truly unopenable -- let the normal failure path handle and report it.
            return pdf_path, None




# =========================================================================
# CORE: PDF -> MARKDOWN
# =========================================================================

def convert_pdf_to_markdown(pdf_path: Path, images_dir: Path, logger: Logger, read_path: Path = None):
    """
    Converts a single PDF into a Markdown string.
    Iterates pages one at a time; if a page throws, it's logged and a
    placeholder is inserted instead of dropping it silently.

    pdf_path: original PDF path -- used for display/naming only.
    read_path: the actual file to open for reading (may be a decrypted/repaired
               temp copy of pdf_path). Defaults to pdf_path if not given.

    Returns: (markdown_text, pages_ok, pages_failed, n_tables, n_images)
    """
    if read_path is None:
        read_path = pdf_path

    pdf_stem = pdf_path.stem
    md_parts = []
    pages_ok = 0
    pages_failed = 0
    n_tables = 0
    n_images = 0

    md_parts.append(f"# {pdf_stem}\n")
    md_parts.append(f"*Converted from `{pdf_path.name}` on "
                     f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")

    # Open with both libraries. If either fails to open entirely, that's a hard failure for this file.
    plumber_doc = pdfplumber.open(str(read_path))
    fitz_doc = fitz.open(str(read_path))

    total_pages = len(plumber_doc.pages)

    # Estimate "body" font size across doc using fitz, for heading heuristics.
    body_size_estimate = 10.0
    try:
        sizes = []
        for p in fitz_doc:
            for block in p.get_text("dict").get("blocks", []):
                for line in block.get("lines", []):
                    for span in line.get("spans", []):
                        sizes.append(span.get("size", 10.0))
        if sizes:
            sizes.sort()
            body_size_estimate = sizes[len(sizes) // 2]  # median
    except Exception:
        pass  # fall back to default estimate

    for page_idx in range(total_pages):
        page_num = page_idx + 1
        try:
            md_parts.append(f"\n<!-- page {page_num} -->\n")

            # ---- Tables first via pdfplumber, so we know which text to suppress later ----
            page_tables_md = []
            table_cell_texts = set()
            try:
                plumber_page = plumber_doc.pages[page_idx]
                tables = plumber_page.extract_tables()
                for t_idx, table in enumerate(tables):
                    if not table:
                        continue
                    md_table = table_to_markdown(table)
                    if md_table:
                        page_tables_md.append((t_idx, md_table))
                        n_tables += 1
                        for row in table:
                            for cell in (row or []):
                                if cell:
                                    norm = " ".join(str(cell).split())
                                    if norm:
                                        table_cell_texts.add(norm)
            except Exception as e:
                logger.log(f"      [table warn] page {page_num}: {e}")

            # ---- Unified text pass via PyMuPDF: detect headings inline, skip lines ----
            # ---- that are purely table-cell content (already captured as a table)  ----
            page_added_content = False
            try:
                fitz_page = fitz_doc[page_idx]
                text_dict = fitz_page.get_text("dict")
                body_lines = []
                for block in text_dict.get("blocks", []):
                    for line in block.get("lines", []):
                        spans = line.get("spans", [])
                        if not spans:
                            continue
                        line_text = "".join(s.get("text", "") for s in spans).strip()
                        if not line_text:
                            continue
                        norm_line = " ".join(line_text.split())
                        # Skip lines that are exactly a table cell's text (avoid duplicating
                        # the table contents as loose paragraph text right above/below it).
                        if norm_line in table_cell_texts:
                            continue
                        # Fallback: if this page has a table, also drop short standalone
                        # tokens (<= 3 chars, no spaces) sitting outside any paragraph --
                        # these are near-always leaked table-cell fragments where pdfplumber
                        # and fitz disagree on the exact glyph (e.g. Symbol-font characters
                        # like lambda/omega get mis-decoded differently by each library).
                        if table_cell_texts and len(norm_line) <= 3 and " " not in norm_line:
                            continue

                        max_size = max(s.get("size", 10.0) for s in spans)
                        level = guess_heading_level(max_size, body_size_estimate)
                        if level > 0 and len(line_text) < 150:
                            body_lines.append(f"\n{'#' * (level + 1)} {line_text}\n")
                        else:
                            body_lines.append(line_text)

                if body_lines:
                    # Join plain consecutive lines into paragraph-ish text, but keep
                    # heading lines (which already carry their own blank-line spacing) intact.
                    out = []
                    buf = []
                    for ln in body_lines:
                        if ln.startswith("\n#"):
                            if buf:
                                out.append(clean_text_block(" ".join(buf)))
                                buf = []
                            out.append(ln)
                        else:
                            buf.append(ln)
                    if buf:
                        out.append(clean_text_block(" ".join(buf)))
                    page_text = "\n".join(o for o in out if o.strip())
                    if page_text.strip():
                        md_parts.append(page_text + "\n")
                        page_added_content = True
            except Exception as e:
                logger.log(f"      [text warn] page {page_num}: {e}")
                # Fall back to pdfplumber's plain text extraction if the fitz pass broke.
                try:
                    plumber_page = plumber_doc.pages[page_idx]
                    raw_text = plumber_page.extract_text() or ""
                    cleaned = clean_text_block(raw_text)
                    if cleaned:
                        md_parts.append(cleaned + "\n")
                        page_added_content = True
                except Exception as e2:
                    md_parts.append(f"*[Text extraction failed for this page: {e2}]*\n")

            if not page_added_content and not page_tables_md:
                md_parts.append("*[No extractable text on this page — possibly an image-only page]*\n")

            # ---- Emit tables (already extracted above) ----
            for t_idx, md_table in page_tables_md:
                md_parts.append(f"\n**Table {t_idx + 1} (page {page_num}):**\n")
                md_parts.append(md_table + "\n")

            # ---- Images via PyMuPDF ----
            try:
                fitz_page = fitz_doc[page_idx]
                img_list = fitz_page.get_images(full=True)
                for img_idx, img_info in enumerate(img_list):
                    xref = img_info[0]
                    try:
                        base_image = fitz_doc.extract_image(xref)
                        image_bytes = base_image.get("image")
                        img_w = base_image.get("width", 0)
                        img_h = base_image.get("height", 0)
                        if not image_bytes:
                            continue
                        if img_w < MIN_IMAGE_DIMENSION or img_h < MIN_IMAGE_DIMENSION:
                            continue
                        ext = base_image.get("ext", "png")
                        fname = f"{pdf_stem}_p{page_num}_img{img_idx + 1}.{ext}"
                        fpath = images_dir / fname
                        with open(fpath, "wb") as f:
                            f.write(image_bytes)
                        rel_path = f"{pdf_stem}{IMAGES_SUBDIRNAME}/{fname}"
                        md_parts.append(f"\n![{fname}]({rel_path})\n")
                        n_images += 1
                    except Exception as e:
                        logger.log(f"      [image warn] page {page_num} img {img_idx+1}: {e}")
                        continue
            except Exception as e:
                logger.log(f"      [image warn] page {page_num}: {e}")

            pages_ok += 1

        except Exception as e:
            # Whole-page failure: never skip silently -- record it.
            pages_failed += 1
            tb = traceback.format_exc(limit=2)
            logger.log(f"      [PAGE FAILED] page {page_num}: {e}")
            md_parts.append(
                f"\n> **[PAGE {page_num} FAILED TO CONVERT]**\n"
                f"> Error: `{e}`\n"
            )
            continue  # move on, don't abort the file

    try:
        plumber_doc.close()
    except Exception:
        pass
    try:
        fitz_doc.close()
    except Exception:
        pass

    md_parts.append(f"\n---\n*End of document. Pages processed: {pages_ok}/{total_pages} "
                     f"({pages_failed} page(s) had errors).*\n")

    return "\n".join(md_parts), pages_ok, pages_failed, n_tables, n_images, total_pages


# =========================================================================
# MARKDOWN -> OBSIDIAN-DARK HTML
# =========================================================================

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
:root {{
    --bg: #1e1e2e;
    --bg-secondary: #181825;
    --bg-elevated: #25253a;
    --text: #cdd6f4;
    --text-muted: #9399b2;
    --accent: #89b4fa;
    --accent-2: #cba6f7;
    --accent-3: #94e2d5;
    --warn: #f9e2af;
    --error: #f38ba8;
    --border: #313244;
    --code-bg: #11111b;
}}

* {{ box-sizing: border-box; }}

html, body {{
    margin: 0;
    padding: 0;
    background: var(--bg);
    color: var(--text);
    font-family: -apple-system, "Segoe UI", "Inter", Helvetica, Arial, sans-serif;
    line-height: 1.7;
}}

.page-wrapper {{
    max-width: 880px;
    margin: 0 auto;
    padding: 48px 32px 96px;
}}

.top-meta {{
    color: var(--text-muted);
    font-size: 0.85em;
    border-bottom: 1px solid var(--border);
    padding-bottom: 16px;
    margin-bottom: 32px;
}}

h1, h2, h3, h4, h5, h6 {{
    color: var(--accent);
    font-weight: 600;
    margin-top: 1.6em;
    margin-bottom: 0.6em;
    letter-spacing: -0.01em;
}}

h1 {{
    font-size: 2.1em;
    border-bottom: 2px solid var(--accent);
    padding-bottom: 0.3em;
    color: var(--accent-2);
}}

h2 {{ font-size: 1.6em; border-bottom: 1px solid var(--border); padding-bottom: 0.25em; }}
h3 {{ font-size: 1.3em; color: var(--accent-3); }}
h4 {{ font-size: 1.1em; color: var(--text); }}

p {{ margin: 1em 0; color: var(--text); }}

a {{ color: var(--accent); text-decoration: none; border-bottom: 1px dotted var(--accent); }}
a:hover {{ color: var(--accent-2); }}

strong {{ color: var(--accent-3); }}
em {{ color: var(--text-muted); }}

blockquote {{
    border-left: 3px solid var(--warn);
    background: var(--bg-elevated);
    margin: 1.2em 0;
    padding: 0.8em 1.2em;
    border-radius: 0 6px 6px 0;
    color: var(--text-muted);
}}

blockquote strong {{ color: var(--error); }}

code {{
    background: var(--code-bg);
    color: var(--accent-3);
    padding: 0.15em 0.4em;
    border-radius: 4px;
    font-family: "JetBrains Mono", "Fira Code", Consolas, monospace;
    font-size: 0.9em;
}}

pre {{
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px;
    overflow-x: auto;
}}

pre code {{ background: none; padding: 0; }}

hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: 2.5em 0;
}}

img {{
    max-width: 100%;
    border-radius: 8px;
    border: 1px solid var(--border);
    margin: 1em 0;
    display: block;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
    background: var(--bg-elevated);
    border-radius: 8px;
    overflow: hidden;
    font-size: 0.92em;
}}

th, td {{
    border: 1px solid var(--border);
    padding: 8px 12px;
    text-align: left;
}}

th {{
    background: var(--bg-secondary);
    color: var(--accent);
    font-weight: 600;
}}

tr:nth-child(even) td {{ background: rgba(255,255,255,0.02); }}

ul, ol {{ padding-left: 1.6em; }}
li {{ margin: 0.3em 0; }}

::selection {{ background: var(--accent); color: var(--bg); }}

.scroll-top {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: var(--accent);
    color: var(--bg);
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 1.2em;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    opacity: 0.85;
    user-select: none;
}}
.scroll-top:hover {{ opacity: 1; }}

@media (max-width: 600px) {{
    .page-wrapper {{ padding: 24px 16px 64px; }}
    h1 {{ font-size: 1.6em; }}
}}
</style>
</head>
<body>
<div class="page-wrapper">
<div class="top-meta">Source: {source_name} &nbsp;|&nbsp; Converted: {converted_time} &nbsp;|&nbsp; Pages: {pages_ok}/{total_pages} ({pages_failed} failed)</div>
{body}
</div>
<div class="scroll-top" onclick="window.scrollTo({{top:0, behavior:'smooth'}})">&#8593;</div>
</body>
</html>
"""


def markdown_to_obsidian_html(markdown_text: str, title: str, source_name: str,
                               pages_ok: int, pages_failed: int, total_pages: int) -> str:
    """Render markdown text into the dark Obsidian-style HTML template."""
    body_html = md_lib.markdown(
        markdown_text,
        extensions=["extra", "sane_lists", "toc", "nl2br"],
    )
    return HTML_TEMPLATE.format(
        title=html_lib.escape(title),
        source_name=html_lib.escape(source_name),
        converted_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        pages_ok=pages_ok,
        pages_failed=pages_failed,
        total_pages=total_pages,
        body=body_html,
    )


# =========================================================================
# MAIN DRIVER
# =========================================================================

def find_base_dir() -> Path:
    """Use CLI arg if given, otherwise the script's own folder."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).resolve()
    return Path(__file__).resolve().parent


def main():
    base_dir = find_base_dir()
    input_dir = base_dir / INPUT_DIRNAME
    output_md_dir = base_dir / OUTPUT_MD_DIRNAME
    output_html_dir = base_dir / OUTPUT_HTML_DIRNAME

    output_md_dir.mkdir(parents=True, exist_ok=True)
    output_html_dir.mkdir(parents=True, exist_ok=True)

    # Scratch space for decrypted/repaired PDF copies (cleaned up at the end).
    tmp_dir = base_dir / ".pdf_conversion_tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    logger = Logger(output_md_dir / LOG_FILENAME)

    logger.log("=" * 78)
    logger.log("  InputToOutputMachine -- PDF -> Markdown + Obsidian-dark HTML")
    logger.log("=" * 78)
    logger.log(f"  Base dir : {base_dir}")
    logger.log(f"  Input    : {input_dir}")
    logger.log(f"  Out (md) : {output_md_dir}")
    logger.log(f"  Out (html): {output_html_dir}")
    logger.log("")

    if not input_dir.exists():
        logger.log(f"  ERROR: input folder not found at {input_dir}")
        logger.write()
        sys.exit(1)

    pdf_files = sorted(input_dir.glob("*.pdf")) + sorted(input_dir.glob("*.PDF"))
    pdf_files = sorted(set(pdf_files))

    if not pdf_files:
        logger.log(f"  No PDF files found in {input_dir}")
        logger.write()
        return

    logger.log(f"  Found {len(pdf_files)} PDF(s) to convert:\n")
    for p in pdf_files:
        logger.log(f"    - {p.name}")
    logger.log("")

    for pdf_path in pdf_files:
        logger.log("-" * 78)
        logger.log(f"  Processing: {pdf_path.name}")
        pdf_stem = pdf_path.stem

        # images live alongside the .md, in <stem>_images/
        images_dir = output_md_dir / f"{pdf_stem}{IMAGES_SUBDIRNAME}"
        images_dir.mkdir(parents=True, exist_ok=True)

        # Try to auto-decrypt (blank password) or auto-repair before the real conversion.
        usable_path, prep_note = prepare_openable_pdf(pdf_path, tmp_dir, logger)
        if prep_note:
            logger.log(f"    [pre-process] {prep_note}")

        try:
            markdown_text, pages_ok, pages_failed, n_tables, n_images, total_pages = \
                convert_pdf_to_markdown(pdf_path, images_dir, logger, read_path=usable_path)

            # Write Markdown
            md_out_path = output_md_dir / f"{pdf_stem}.md"
            md_out_path.write_text(markdown_text, encoding="utf-8")
            logger.log(f"    -> wrote {md_out_path.name}  "
                       f"(pages ok: {pages_ok}/{total_pages}, tables: {n_tables}, images: {n_images})")

            # Write HTML
            html_text = markdown_to_obsidian_html(
                markdown_text,
                title=pdf_stem,
                source_name=pdf_path.name,
                pages_ok=pages_ok,
                pages_failed=pages_failed,
                total_pages=total_pages,
            )
            html_out_path = output_html_dir / f"{pdf_stem}.html"
            html_out_path.write_text(html_text, encoding="utf-8")
            logger.log(f"    -> wrote {html_out_path.name}")

            # Mirror the images folder next to the HTML file too, so the HTML
            # is self-contained and images actually render when opened
            # (the .md and .html live in different folders, so each needs its own copy).
            if n_images > 0 and images_dir.exists() and any(images_dir.iterdir()):
                html_images_dir = output_html_dir / f"{pdf_stem}{IMAGES_SUBDIRNAME}"
                try:
                    if html_images_dir.exists():
                        shutil.rmtree(html_images_dir)
                    shutil.copytree(images_dir, html_images_dir)
                except Exception as e:
                    logger.log(f"    [image copy warn] could not mirror images to html dir: {e}")

            status = "OK" if pages_failed == 0 else "WARN"
            logger.add_summary(pdf_path.name, status, pages_ok, pages_failed, n_tables, n_images)

            # Clean up empty images dir if nothing was extracted (no clutter).
            if n_images == 0 and images_dir.exists() and not any(images_dir.iterdir()):
                try:
                    images_dir.rmdir()
                except Exception:
                    pass

        except Exception as e:
            # Whole-FILE failure (e.g. corrupt/encrypted PDF that won't even open).
            # We still never crash the batch -- log it and move to the next file.
            tb = traceback.format_exc()
            logger.log(f"    [FILE FAILED] {pdf_path.name}: {e}")
            logger.log(f"    {tb.splitlines()[-1] if tb else ''}")

            # The images dir was pre-created before we knew this file would fail; remove if empty.
            if images_dir.exists() and not any(images_dir.iterdir()):
                try:
                    images_dir.rmdir()
                except Exception:
                    pass

            # Write a placeholder md/html so the failure is visible in the output folders too.
            fail_md = (
                f"# {pdf_stem}\n\n"
                f"> **CONVERSION FAILED**\n>\n"
                f"> This PDF could not be opened or processed.\n>\n"
                f"> Error: `{e}`\n>\n"
                f"> This may mean the file is corrupted, password-protected, "
                f"or not a valid PDF. Try opening it manually to check.\n"
            )
            (output_md_dir / f"{pdf_stem}.md").write_text(fail_md, encoding="utf-8")
            fail_html = markdown_to_obsidian_html(
                fail_md, title=pdf_stem, source_name=pdf_path.name,
                pages_ok=0, pages_failed=0, total_pages=0,
            )
            (output_html_dir / f"{pdf_stem}.html").write_text(fail_html, encoding="utf-8")

            logger.add_summary(pdf_path.name, "FAIL", 0, 0, 0, 0, note=str(e)[:60])

    logger.print_summary()

    # Clean up temp decrypted/repaired copies.
    try:
        shutil.rmtree(tmp_dir, ignore_errors=True)
    except Exception:
        pass

    logger.write()
    logger.log(f"\nFull log saved to: {logger.log_path}")


if __name__ == "__main__":
    main()
