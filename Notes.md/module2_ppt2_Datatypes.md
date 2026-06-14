# Lecture/Document: module2_ppt2_Datatypes

## Page 1
UNIT 2: DATA TYPES
Prachi Surlakar
Assistant Professor
Computer Engineering Department
Goa College of  Engineering


## Page 3
DATATYPES IN PYTHON
Simple python program
Output:


## Page 4
COMMENTS IN PYTHON
There are two types of  comments in python
1. Single line comments    2.    Multiline comments
1. Single line comments 
• These comments start with a hash(#) 
symbol
• Entire line till the end must be treated as 
comment.
Comments are non executable statements. It means neither python compiler nor PVM will 
execute them. 
2. Multiline comments
Triple double quotes(“ “ “)
Triple single quotes(‘ ‘ ‘)
“ “ “
Web technology encompasses the various tools 
and techniques used to create, websites.
 “ “ “
‘ ‘ ‘ 
Web technology encompasses the various tools 
and techniques used to create websites.
‘ ‘ ‘


## Page 5
DOCSTRINGS
• Triple double quotes(“ “ “) OR Triple single quotes(‘ ‘ ‘) are actually not multiline 
comments but they are regular strings with the exception that they can span multiple 
lines.
• So using Triple double quotes(“ “ “) OR Triple single quotes(‘ ‘ ‘) are not 
recommended for comments in python as they internally occupy memory and would 
waste time of  interpreter.
• If  we write strings inside Triple double quotes(“ “ “)OR Triple single quotes(‘ ‘ ‘) and if  
these strings are written as first statements in a module, function or a method, then these 
strings are called as documentation strings or docstrings
• Docstrings are used to create API( application programming interface) 
documentation file.
• An API documentation file is a text file or html file that contains all features of  
software, language or a product


## Page 6
Assigning values
a=10
b=15
Identifier: names of  variables, functions ,objects etc.
In C or java
int a;
a=10
In python we need not declare the datatype of  variable explicitly
a=10


## Page 7
DATATYPES IN PYTHON
Built in datatypes
• Datatypes already available in python are called as built in datatypes.
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings


## Page 8
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
The None Type
• ‘NoneType’ datatype represents an object that does 
not contain any value.
• It is used inside a function as a default value of  the 
arguments
• When calling the function, if  no value is passed the 
default value will be taken as none 
• In Boolean none value represents false.
def  greet(name=None):
    if  name is None:
        print("Hello, Stranger!")
    else:
        print("Hello, {name}!")
greet( )         # Output: Hello, Stranger!
greet("Alice")  # Output: Hello, Alice!


## Page 9
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
 int Type
• Represents an integer number.
• Without any decimal point  or fraction part
• Example: 200,-50, 0
a=50
No limit for the size of  the datatype
There are  3 subtypes of  
numeric
• int 
• float
• complex
float type
• Floating point numbers
• Number that contains decimal point
• Example:  0.5, -3.5667
• Can also be written in scientific notation using ‘e’ 
or ‘E’ e.g: 2.5E4
• num=55.7


## Page 10
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
 Complex Datatype
• Written in the form a+bj or a+bJ
• ‘a’ represents real part of  the number and ‘b’ represents 
the imaginary part.
• ‘a’ and ‘b’ may contain integers or floats
• Example: 3+5j, -1-5.5J
C1=-1-5.5J
There are  3 subtypes of  
numeric
• int 
• float
• complex
Output:


## Page 11
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
 Representing binary, octal and hexadecimal numbers
• Binary number: prefix 0b or 0B
     0b11110001  , 0B11100110
• Hexadecimal number: prefix 0x or 0X
    0xA180 , 0X11fb91
• Octal numbers: Prefix 0o or 0O
    0O145 ,0o773There are  3 subtypes of  
numeric
• int 
• float
• complex


## Page 12
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
 Converting datatypes explicitly
• Python internally assumes datatype of  the variable.
• If  programmer converts one datatype into another 
datatype on its own it is called as type conversion.
There are  3 subtypes of  
numeric
• int 
• float
• complex


## Page 13
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
 Converting datatypes explicitly
• Python internally assumes datatype of  the variable.
• If  programmer converts one datatype into another 
datatype on its own it is called as type conversion.
There are  3 subtypes of  
numeric
• int 
• float
• complex
complex(x) will convert x into a complex number
complex(x,y) will convert x and y into a complex number


## Page 14
A program to convert numbers from octal , binary and hexadecimal systems into 
decimal number system (Method 1)
OUTPUT


## Page 15
Exercise 1:
Write a python program to convert the following numbers in decimal number system.
(a) Octal number 5  (b)Binary number 0010   (c) Hexadecimal number E
OUTPUT:


## Page 16
Function  int(string,base) is useful to convert a string into a decimal/ integer.
A program to convert numbers from octal , binary and hexadecimal systems into 
decimal number system( Method 2)
OUTPUT:


## Page 17
Exercise 2:
Write a python program USING int(string,base) to convert the following numbers in decimal number 
system.
(a) Octal number 5  (b)Binary number 0010   (c) Hexadecimal number E
OUTPUT:


## Page 18
bin( ): convert number to binary
oct( ): convert number to octal
hex ( ): convert number to hexadecimal
Write a python program to convert 10 to binary, octal and hexadecimal


## Page 19
Bool datatype
• Bool datatype in python represents boolean values.
• There are only 2 Boolean values True or false
• True:1 and false: 0
• Conditions will be evaluated internally to either true or false.


## Page 20
Bool datatype
• Bool datatype in python represents boolean values.
• There are only 2 Boolean values True or false
• True:1 and false: 0
• Conditions will be evaluated internally to either true or false.


## Page 21
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
str Datatype
• String is a group of  characters. 
• Strings are enclosed in single or double quotes
We can also write strings inside Triple double quotes(“ “ “) or 
Triple single quotes(‘ ‘ ‘) to span a group of  lines, including 
spaces.


## Page 22
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
Triple double quotes(“ “ “) or Triple single quotes(‘ ‘ ‘) 
are useful to embed a string inside another string
str= “ “ “ This is ‘ Core Python ’ book ” ” ”
print(str)  
#will display : This is ‘Core Python’ book
str ‘ ‘ ‘This is “Core Python” book ’ ’ ’
print(str) 
 #will display : This is “Core Python” book


## Page 23
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
• Square brackets [ ]are used to retrieve pieces of  a string.
• Characters in a string are counted from zero onwards 
• E.g. str[0] indicates the beginning character
• * is repetition character


## Page 24
• Square brackets [ ]are used to retrieve pieces of  a string.
• Characters in a string are counted from zero onwards 
• * is repetition character
str Datatype
w e l c o m e t o c o r e . …
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
s = 'welcome to python'
print((s + ' ') * 2)


## Page 25
Write a python program to perform the following operations on strings
a) Take a string as hello world
b) Display the first character
c) Display hello
d) Display world
e) Print the last character


## Page 26
Write a python program to perform the following operations on strings
a) Take a string as hello world
b) Display the first character
c) Display hello
d) Display world
e) Print the last character
f) Print string in reverse


## Page 27
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
Bytes datatype
• Represents a group of  byte numbers like an array does
• Byte number is any positive integer from 0 to 255
• Cannot store negative numbers
• We cannot modify or edit any element in the bytes array.
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings


## Page 28
Write a python program to create a byte type array, read and display the elements of  the array
OUTPUT
Bytes datatype


## Page 29
Write a python program to create a byte type array, read and display the elements of  the array
OUTPUT
Bytes datatype


## Page 30
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
Bytearray datatype
• Similar to bytes datatype
• Difference is that bytes type array cannot be modified but 
bytearray can be modified.
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings


## Page 31
Bytearray datatype
Write a program to create a bytearray type array with elements as [10,20,0,40,15]. Modify the first 
two elements and retrieve the elements.
OUTPUT


## Page 32
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
List datatype
• List represents a group of  elements
• List can store different types of  elements but an array 
can store only one type of  elements.
• List can grow dynamically but size of  array is fixed.
• Slicing operation like [0:3] represents elements from 
0th to 2nd positions.
• i.e: 10, 20, 15.5
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings


## Page 33
List datatype


## Page 34
List datatype
Write a program to create a list with the following elements[ 10, 20, “ abc”, “xyz”]. Perform the 
following operations
a) Print all the list elements
b) Print the first element
c) Print first two elements
d) Print second and third element
e) Print last element
f) Print list two times
OUTPUT


## Page 35
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
Tuple datatype
• Tuple contains a group of  elements which can be of  
different types.
• Elements of  a tuple a written inside ( )
• Difference between a list is that the list elements can be 
modified but tuple elements cannot be modified. It is 
a read only list.
• Individual elements of  the tuple can be referenced 
using square braces as tp1[0], tp1[2]….
WE CANNOT MODIFY TUPLE ELEMENTS
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings


## Page 36
Tuple datatype
Write a program to create a tuple with the following elements[ 10, 20, “ abc”, “xyz”]. Perform the 
following operations
a) Print all the tuple elements
b) Print the first element
c) Print first two elements
d) Print second and third element
e) Print last element
f) Print tuple two times
OUTPUT


## Page 37
Tuple datatype
Write a program to create a tuple with the following elements[ 10, 20, “ abc”, “xyz”]. Perform the 
following operations
a) Print all the list elements
b) Print the first element
c) Print first two elements
d) Print second and third element
e) Print last element
f) Print list two times
g) Modify first element to 99


## Page 38
There are  6 subtypes of  
sequences
• str 
• bytes
• bytearray
• list 
• Tuple
• range
range  datatype
• range datatype represents a sequence of  numbers.
• Example:
r = range(10)
 #will create a range with number starting from 0 to 9
#We can display the numbers using a for loop
 for i in r : print(i)  # will display numbers from 0 to 9
r=range(30,40,2)
for i in r: print(i)
Will display   30,32,34,36,38  # starting with 30 till 39
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences( group of  elements)
4. Sets
5. Mappings
We can create a list with a range of  numbers from 0 to 9


## Page 39
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
There are two subtypes in sets
• set datatype
• frozenset datatype
Set datatype
To create a set you should enter the elements separated 
by commas inside curly braces { }
• Set is not maintaining order
• Set does not store duplicate elements
• We can convert a list into a set using the set function


## Page 40
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
There are two subtypes in sets
• set datatype
• frozenset datatype
Set datatype
• update( ) method is used to add elements to the set
• remove( ) method is used to remove any particular 
element from the set.
Since set is unordered we cannot retrieve the 
elements using indexing operations
CANNOT BE USED


## Page 41
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
There are two subtypes in sets
• set datatype
• frozenset datatype
frozenset datatype
• Similar to set datatype
• Difference is that elements in set datatype can be modified 
but elements in frozenset datatype cannot be modified.
• Example:
Another way of  creating a frozen set is by passing a string (group of  
characters) to the frozen set.
fs=frozenset(“abcdefg”)
print(fs) # may display frozenset({‘e’ ,’g’ ,’f ’, ‘d’, ‘a’, ‘c’, ‘b’})
Update( ) and remove( ) methods will not work on frozen 
sets as they cannot be modified
s={10, 20, 30,50}
fs= frozenset(s) # create frozenset
print(fs)  
Output:


## Page 42
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
Mapping types
• Map represents a group of  elements in the form of  key/value 
pairs
• dict datatype is an example for a map: dict represents a 
dictionary that contains pairs of  elements such that first element 
represents the key and the next one becomes its value.
• COLON ( : )to separate key and value.
• Pair separated by comma.
• All elements inside curly brackets.
• Example: roll no and names of  students.
 d={10 : ‘Rohan’ , 11: ‘Krishna’ ,12: ‘Ram’}
OR
An empty dictionary can be created
d= { } 
Later we can store key and values into d as
d[10] : ‘ Rohan’ 
d[11] : ‘ Krishna’
print(d) 
Will display
{10 :’Rohan’ , 11: ‘Krishna}


## Page 43
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
Mapping types
Performing operations:
d[key] :To retrieve values upon giving the keys 
keys( ) : to retrieve only keys
values( ) : to retrieve only values
d[key]=newvalue : to update value 
del d[key] : will delete key along with its values


## Page 44
Mapping types
del


## Page 45
Literals in python
Literal is a constant value that is stored into a 
variable in a program.
Example:
a =10
Following are different types of  literals in python
• Numeric literals
• Boolean literals
• String literals


## Page 46
Literals in python
Types of  literals in python
• Numeric literals
• Boolean literals
• String literals
• Numeric literals


## Page 47
Literals in python
Types of  literals in python
• Numeric literals
• Boolean literals
• String literals
Boolean literals
• Boolean literals are the true or false values stored 
into a bool type variable


## Page 48
Literals in python
Types of  literals in python
• Numeric literals
• Boolean literals
• String literals
String literals
• A group of  characters is called a string literal
• String literals are enclosed in 
❑ single quotes(‘ )
❑ Double quotes(“ )
❑ Triple quotes(’’’ or ”””)
In python there is no difference between single 
quoted strings and double quoted strings
    


## Page 49
Literals in python
Types of  literals in python
• Numeric literals
• Boolean literals
• String literals
String literals
• When a string literal extends beyond a single line 
we should use triple quotes
    
If  you want to use double quotes and a string spans 
more than one line adding Backslash(\) will join next 
string to it.


## Page 50
String literals


## Page 51
Determining the datatype of  a variable
• To know the datatype of  a variable or object we can use the type( ) function.
Every datatype, function, method, class, lists,sets etc are all objects in python.
OUTPUT:


## Page 52
Determining the datatype of  a variable
• Determining type for characters
Python does not have a char datatype to represent individual characters.
It has str datatype which represents strings. 
# will display B
 #will display true
# will display false


## Page 53
User defined datatypes
Datatypes which are created by programmers are called user defined datatypes.
Example: 
Array, class etc are user defined datatypes
Mod 3


## Page 54
Constants in python
• Constant is similar to a variable but its value cannot be changed or modified.
• Once defined a constant cannot allow changing its value.
• A programmer can indicate a variable as constant by writing its name in capital letters.


## Page 55
Identifiers and reserved words
Identifiers
• Is a name given to a variable or function or class etc.
• Can include letters, numbers  and underscore(_)
• Always start with a non numeric character.
• Special symbols such as ?, # $, %, and @ are not allowed.
• Examples: salary, abc11,  abc_x etc.
• Python is case sensitive language.
• Num and num are treated as different names.


## Page 56
Identifiers and reserved words


## Page 57
Reserved words
Reserved words should not be used as identifiers.


## Page 58
Naming Conventions in Python
• Rules related to  writing names of  packages, modules, classes, variables etc are called naming conventions.
• The following naming conventions should be followed.
1. Packages: Packages names should be written in all lower case letters. When multiple words are used for a 
name, we should separate them using an underscore( _ ).
2. Modules: Module names should be written in all lower case letters. When multiple words are used for a 
name, we should separate them using an underscore( _ ).
3. Classes: Each word of  a class name should start with a capital letter.(rule applicable to the class created by 
us).Pythons build in class names use all lowercase letters.( eg: int, str, list etc.)
4. Global variables or module level variables: should be written in all lower case letters. When multiple 
words are used for a name, we should separate them using an underscore( _ ).
5. Instance variables: should be written in all lower case letters. When multiple words are used for a name, 
we should separate them using an underscore( _ ).
6. Functions: should be written in all lower case letters. When multiple words are used for a name, we should 
separate them using an underscore( _ ).
7. Method arguments:  In case of  instance methods, the first argument name should be ‘self ’. In case of  
class methods, first argument must be ‘cls’.
8. Constants: Constants names should be written in all capital letters. If  there are several words then each 
word must be separated by an underscore( _ ).


## Page 59
SUMMARY OF DATATYPES
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
1. None Type
2. Numeric types
•  int
• float 
• complex
• Conversions(octal ,bin,hex)
• Bool type
3 . sequences
• str 
• bytes : numbers from 0 to 255, cannot modify elements
• bytearray : numbers from 0 to 255, can modify elements
• list : square brackets[ ], contain any type of  elements, can 
modify elements
• tuple : round brackets( ), contain any type of  elements, cannot 
modify elements
• range : creates a range of  numbers


## Page 60
SUMMARY OF DATATYPES
Built in datatypes are of  5 types
1. NoneType
2. Numeric types
3. Sequences
4. Sets
5. Mappings
4. Sets
• set datatype :curly brackets { },  elements unordered, no indexing 
operations, can modify elements.
• frozenset datatype: curly brackets { },  elements unordered, cannot 
modify elements.
5. Mappings: key value pairs, colon operator(:) to separate key and 
value, curly brackets { }


## Page 61
THANK YOU☺
by PRACHI SURLAKAR

