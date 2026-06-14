# Lecture/Document: strings

## Page 1
1 
STRINGS AND CHARACTERS 
A string represents a group of characters. Strings are important because most of the data that we use in daily life will be in the form of strings. For example, the names Lof persons, their addresses, vehicle numbers, their credit card numbers, etc. are all strings. In Python, the str datatype represents a string. 
Creating Strings 
Since every string comprises several characters, Python handles strings and characters almost in the same manner. There is no separate datatype to represent individual characters in Python. 
s1 = 'wel come to Core Python learning! s2 ="Welcome to Core Python learning" 
CHAPTER 
We can create a string in Python by assigning a group of characters to a variable. The group of characters should be enclosed inside single quotes or double quotes as: 
There is no difference between the single quotes and double quotes while creating the strings. Both will work in the same manner. 
str = "'welcome to Core Python, a book on Python 
8 
Sometimes, we can use triple single quotes or triple double quotes to represent strings. These quotation marks are useful when we want to represent a string that occupies several lines as: language that discusses al1 important concepts of Python in a lucid and comprehensive manner. 
Str = n"wel come to Core Python, a book on Python In the preceding statement, the string 'str is created using triple single quotes. Alternately, the above string can be created using triple double quotes as: language that discusses a]1 important 1n a Tucid and comprehensive manner ncepts of Python 

## Page 2
208 Chapter 8 
Thus, triple single quotes or triple double quotes are useful to create strings which Sre 
into sever al lines. 
It is 
possible to display 
quotation marks to mark a sub string in a string. In that caee 
should use one type of quotes for outer string and 
another type of quotes for inner st 
as: 
sl = 
'welcome to "Core 
Python" 
learning' 
print(s1) 
The 
preceding lines of code will display the 
following output: 
welcome to "Core 
Python" 
learning 
Here, the string 's1' 
contains two 
strings. The outer string is 
enclosed in single quotes 
s1 = "wel come to 'Core 
Python' 
learning" 
print (s1) 
The 
welcome to 'Core 
Python' 
learning 
It is 
possible to use 
escape 
characters like t or \n inside the 
strings. The escape 
character \t 
releases tab space of 6 or 8 
spaces and the 
escape 
character \n throws 
Cursor into a new line. For 
example, 
sl = 
"'Welcome 
to\tCore 
Python\nlearning" 
print (S1) 
The 
preceding lines of code will display the 
following output: 
Core Python 
Welcome to learning 
Table 8.1 
summarizes the 
escape 
Table 8.1: Escape 
Characters and their 
Meanings 
Meaning 
Escape Character 
Bell or alert Backspace 
\a \b 
New line 
\n 
Horizontal tab space Vertical tab space Enter button 
\r 
Displays single \ Character x 
x and the inner string, i.e. "Core 
Python" is 
enclosed in double quotes. 
Alternately, we can 
use double quotes for outer string and single quotes for inner string as: 
preceding lines of code will display the 
following output: 
characters that can be used in 
strings: 

## Page 3
Strings and 
Characters 209 
To sl = r"wel come 
to\tcore 
Python\nlearning" 
print(s1) 
The 
preceding lines of code will display the 
following output: 
Welcome to\tCore Python\nlearning 
This is not 
showing the effect of \t or \n. It means we could not see the 
horizontal tab 
space or new line. Raw strings take escape 
characters, like \t, \n, etc., as 
ordinary 
characters in a string and hence display them as they are. 
To create a string with 
Unicode 
characters, we should add u' at the 
beginning of the 
programming 
languages like Python or Java. For 
example, it is possible to display the 
string. Unicode is a 
standard to include the 
alphabet of various human 
languages into 
alphabet of Hindi, French, and 
German 
languages using Unicode system. Each Unicode 
Python' in Hindi using Unicode 
characters. There are 8 
Unicode 
characters used for this 
character 
contains 4 digits 
preceded by a \u. The 
following 
statement displays Core 
purpose. name = 
u'\u0915\u094b\u0930 
\u092a\u0948\u0925\u0964\u0928' 
print (name) 
The 
preceding lines of code will display the 
following output: 
Length of a String 
Length of a string 
represents the 
number of 
characters in a string. To know the length of 
a string, we can use the len() 
function. This 
function gives the 
number of 
characters 
including spaces in the string. str ='Core Python n = len(str) print (n) 
The 
preceding lines of code will display the 
following output: 
11 
Indexing in Strings 
Index 
represents the 
position 
number. Index is 
written using square braces |. By 
Specifying the position number through an index, we can refer to the 
individual elements 
(or 
characters) of a string. For 
example, str[0] refers to the 0th element of the string and 
str|1] refers to the 1st 
element of the string. Thus, strlil can be used to refer to ith 
element 
of the string. Here, is called the string index because it is 
specifying the 
position 
number of the 
element in the string. 
nullity the effect of 
escape 
characters, we can create the string as a raw string by 
addingr before the string as: 

## Page 4
210 Chapter 8 When we use index as a 
ncgative 
number, it refers to 
elenents in the reverse order Ths 
str|-1] refers to the last clement and str-2] refers to second element trom last. Figure 8 1 
shows how the indexes refer to the 
individual clements in the string: 
10 
9 
5 
3 
2 
1 
0 positive indexes 
h 
A 
e 
r 
C 
str 
-1 -2 
-3 
5 
-7 
-8 
-9 -10 
-11 negetive indexes 
Figure 8. I: Indexing in String 
In 
Program 1, we are 
showing how to access each 
element of a string in 
forward and 
reverse orders using the while loop. 
Program 1: A Python program to access each 
element of a string in 
forward and reverse 
orders using while loop. 
# 
indexing on 
strings 
str = 'Core Python 
# 
access each 
character usi ng whi le Toop 
n = 
len(str) # n no. of 
chars in str 
i=0 # i = 
0,1,2,... n-1 print(str[i], end=) 
i+=1 while i<n: # put 
Cursor into next 1ine 
print() 
print(str[i], end' ') 
i-=1 
# 
access in 
reverse 
order 
i=-1 # i = 
-1,-2,-3,.. 
while i=-n: print) # put cursor into next line 
# 
access in 
reverse order using 
negative index 
i=1 # i = 
1,2,3,... n 
n= 
len(str) # n no. of 
chars in str 
while i<=n: 
print(str[-i], end=' ) 
i+=1 Output: 
C:python shon 
Cor e P 
eroC eroC 
n o ht y P noht y P 

## Page 5
We can also use the for loop to access each element (or character) of a string. The following for loop simply takes cach element into a variable i' and displays it. for i in str: print(i) To display the string in the reverse order, we should use slicing operation on string, The format of slicing is stringname<start: stop: stepsize]. If 'start' and stop' are not specified, then it is taken from 0th to n-1 th elements. If 'stepsize' is not written, then it is taken to be 1. Hence, the following loop will display all the elements of the string: for i in str[::]: print(i) To get the elements in reverse order, we should use stepsize negative as: -1. This will display the elenments from last to first in steps of 1 in reverse order. The for loop in this case looks like this: for i in str[:: -1]: # take stepsize as -1 print(i) 
Prona 
This is what we have shown in Program 2. In this program, we used for loop to access the characters of a string in forward direction and then another for loop to access the characters in reverse order. 
# do not mention start, stop and stepsize 
Program 2: A Python program to access the characters of a string using for loop. str = 'Core Python # accessing elements of a string using for l0op # access each Tetter using for loop for i in str: 
Strings and Characters 211 
print(i, end=' ') print(O # put cursor into next 1ine # access in reverse order 
Output: for i in strl::i, print(i, 
C:\>pythons hon Core,p n oht y P er o C 
Slicing the Strings A slice represents a part or piece of a string. The format of slicing is: stringname [start: stop: stepsize] 

## Page 6
212 Chapter 8 If 'start' and 'stop' are not specified. then slicing is done from 0th to n-1th elemen1s 1e 'stepsize' is not written, then it is taken to be 1. See the following example: str = 'Core Python' str[0:9:1] Core Pyth When stepsize' is 2, then it will access every other character from 1st character onwarde Hence it retrieves the Qth, 2nd 4th, 6th characters and so on. str [0:9:23 Cr yh Some other examples are given below to have a better understanding on slicing. Consider the following code snippet: str = 'Core Python' str[::] # access string from 0th to last character The preceding lines of code will display the following output: Core Python If you write, 
# access string from 0th to 8th element in steps of 1 
str[2:4:1] # access from str[2] to str[3] in steps of 1 Then, the following output appears: re If you write the following statement: Str[::2] # access entire string in steps of 2 Then, the following output appears: Cr yhn Now, if you write the following statement: Str[2::] # access string from str[2] to ending Then, the preceding lines of code display the following output: re Python Suppose if you write the following statement: 8 str[:4:1 # access string from str[0] to str[3] in steps of 1 The following output appears: Core It is possible to use reverse slicing to retrieve the elements from the string in revc order. The 'start, 'stop' can be specified as negative numbers. For example, str = 'Core Python! str[-4:-1] # access from str[-4] to str[-2] from left to right in str. The following output appears: tho 

## Page 7
Now, if you write the following statement: The following output appears: str[-6::] # access from str[-6] till the end of the string Python When stepsize is negative, then the elements are counted from right to left. See the examples: 
left 
str[-1: -4:-1] # retrieve from str[-1] to str[-3] from right to left The output of the preceding statement is as follows: 'nohe Now, if you write the following statement: str[-1: :-1] # retrieve from str[-1] till first element from right to The output of the preceding statement is as follows: 'nohtyp eroc' Repeating the Strings The repetition operator is denoted by * symbol and is useful to repeat the string for several times. For example, str *n repeats the string for n times. See the example: str = ' Core Python" print (str*2) The preceding lines of code will display the following output: Core PythonCore Python Similarly, it is possible to repeat a part of the string obtained by slicing as: # repeat 5th 6th characters for 3 times s= str[5:7]*3 print(s) 
Strings and Characters 213 
The output of the preceding statement is as follows: PyPyPy Concatenation of Strings We can use <+ on strings to attach a string at the end of another string. This operator +' is called addition operator when used on numbers. But, when used on strings, it is called 'concatenation' operator since it joins or concatenates the strings. Similar result can be achieved using the join(0 method also which will be discussed a little later. sl='Core s2="Python" S3=sl+s2 # concatenate sl and s2 print (s3) # display the total string s3 

## Page 8
214 Chapter & The output of the preceding statement is as follows: corePython Checking Membership We can check if a string or character is a member of another string or not using in' 'not in' operators. The in' operator returns True if the string or character is found in +he main string. It returns False if the string or character is not found in the main string Tha 'not in' operator returns False if a string or character is not found in the main stio otherwise True. The operators in' and 'not in' make case sensitive compariSons. It means these operators consider the upper case and lower case letters or strings differently while comparing the strings. In Program 3, we input a main string and a sub string from the keyboard and check whether the sub string is found in the main string or not. 
Program 3: A Python program to know whether a sub string exists in main string or not. # to know whether sub string is in main string or not str = input('Enter main string: sub input('Enter sub string: ) if sub in str: print(sub+' is found in main string') else: Output: print(sub+' is not found in the main string') C:\bpython str.py Enter main string: This is Core Python Enter sub string: Core Core is found in main string Comparing Strings 
or 
We can use the relational operators like >, >=, <, <, =-or [= operators to compare to strings. They return Boolean value, i.e. either True or False depending on the string" being compared. sl='Box' s2='BOy' if(sl==s2): print('Both are same') else: print('Not same') This code returns Not same' as the strings are not same. While comparing the strings, Python interpreter compares them by taking them in English dictionary order. The su 

## Page 9
which comes first in the dictionary order will have a low value than the string which comes next. It means, A' is less than B' which is less than C' and so on. In the above example, the string 's1' comes before the string 's2' and hence s1 is less than s2. So, if we write: if sl<S2: print("s1 less than s2') else: print(s1 greater than or equal to s2') Then, the preceding statements will display 'sl less than s2'. Removing Spaces from a String A space is also considered as a character inside a string. Sometimes, the unnecessary spaces in a string will lead to wrong results. For example, a person typed his name Mukesh (observe two spaces at the end of the string) instead of typing Mukesh'. If we compare these twO strings using == operator as: if 'Mukesh '=='Mukesh': print('welcome') else: print('Name not found') The output will be Name not found'. In this way, spaces may lead to wrong results. Hence such spaces should be removed from the strings before they are compared. This is possible using rstrip), lstrip) and strip) methods. The rstrip() method removes the spaces which are at the right side of the string. The lstrip() method removes spaces which are at the left side of the string. strip() method removes spaces from both the sides of the strings. These methods do not remove spaces which are in the middle of the string. Consider the following code snippet: name = Mukesh Deshmukh' #observe spaçes before and after the name print (name.rstrip )) # remove spaces at right The output of the preceding statement is as follows: Mukesh Deshmukh Now, if you write: print (name.1stríp)) 
Strings and Characters 215 
The output of the preceding statement is as follows: Mukesh Deshmukh Now, if you write: 
# remove spaces at left 
print (name. stripO) # remove spaces from both sides The output of the preceding statement is as follows: Mukesh Deshmukh 

## Page 10
216 Chapter & Finding Sub Strings The find). rfind), index) and rindex) methods are useful to locate sub strings in a string. These methods return the location of the first occurrence of the sub string in the mo string. The find( and index() methods search for the sub string from the beginning of the main string. The rfind() and rindex() methods search for the sub string from right to l i.e. in backward order. The find() method returns -1 if the sub string is not found in the main string. The indevn method returns ValueError' exception if the sub string is not found. The format of fndh method is: mainstring. find(substring, beginning, ending) The same format is used for other methods also. In Program 4, we are trying to display the first occurrence of the sub string in the main string by accepting both the strings from the user. In Program 4, we are using find() method. 
Program 4: A Python program to find the first occurrence of sub string in a given main string. # to find first occurrence of sub string in a main string str = input('Enter main string: sub = input('Enter sub string: # find position of sub in str # search from 0th to last characters in str n = str.find(sub, 0, len(str)) # findO returns -1 if sub string is not found if n == -1: else: Qutput: print('Sub string not found') print('sub string found at position:', n+1) C:\>python str.py Enter main string: This is a book Enter sub string: is Sub string is found at position: 3 In the above program, observe that the Sub string position is displayed to be at n. Since find() method starts counting from Qth position and we count from 1st position, w need to add 1 to the result given by find() method to get correct position number. The same program can be rewritten using index() method. If the sub string is not found, index) method returns ValueError' exception, we have to handle the exception in ou program. This is what we did in Program 5. 

## Page 11
Preram Program 5: A Python program to find the first 0CCurrence of sub string in a given string using index() method. # to find first occurrence of sub string in a main string str = input(Enter main string: sub = input('Enter sub string: ) # find position of sub in str #search from 0th to last characters in str try: n = str.index (sub, 0, len(str)) except ValueError: else: Output: 
print('Sub string not found ) 
Same as in case of Program 4.E print('Sub string found at position: 
Prorsm 
The find() method and index) methods return only the first occurrence of the sub string, When the sub string occurs several times in the main string, they cannot return all those occurrences. Is there any way that we can find out all the occurrences of the sub string is the question. For this purpose, we should develop additional logic. Initialy, searching should start from 0h character in the main string 'str' up to the last character n' which is given by len(str). So, T value will start initially at 0. When the ind) method finds the position of the sub string, we should display it. Suppose the sub string is found at 2nd position, then we need not again search for the sub string up to the 2nd position. This time, we should continue searching from 3rd character onwards. Thus, 1 value will become 3 i.e. i = pos+1. If find) method could not find the sub string, then normal incrementing of i is done, i.e. i= i+1. This logic is used in Program 6. 
Program 6: A Python program to display all positions of a sub string in a given main string. str = input('Enter main string: i=0 
Strings and Characters 217 
# to fi nd all occurrences of sub string in a main string sub = input('Enter sub string: 
n+1) 
flag=False # becomes True if sub string is found n = len(str) pos = str.find(sub, i, n) while i<n: # repeat from Oth to nth characters if pos != -1: # if found di splay its print('Found at position: else: pos+15STtion i=pos+1 # search from pos+1 position onwards flag=True i=i+l # search from next character onwards 

## Page 12
218 Chapter & if flag == False: Output: print('Sub string not found') C:\>python str.py Enter main string: This is a book Enter sub string: is Found at position: Found at position: The above program can be simplificd by taking 'pos' value initially as -1 and rewritine find) method as: pos = str.find(sub, pos+l, n) First time, find() method will start searching from 0th to nth character since 'pos = -1' # the sub string is found, then its position is assigned to pos' and hence the next time find) method will search from 'pos+ l1' till the end of the string. In this way, when the suh string position is found, find() method will continue searching frorn its next position onwards. If the string is found not even once, then pos' value will continue to be -1 and hence we can break the loop as: if pos =-1: break This logic is used in Program 7 which gives samne output as the Program 6. 
Progranm 7: A program to display all positions of a sub string in a given main string version 2. # to find all occurrences of sub string in a main string -v2.0 str = input('Enter main string: sub = input('Enter sub string: ) flag=False pos = -1 n = len(str) while True: # repeat forever pos = str.find(sub, pos+l, n) if pos == -1: break print(" Found at positi on: flag=True if flag==False: print('Not found') Counting Substrings in a String 
, pos+1) 
The method cOunt() 1s available to count the number of occurrences of a sub string main string. The format of this method is: stringname.count (substring) 

## Page 13
This returns an integer number that represents how many times the substring is found in the main string. We can limit our search by specifying beginning and ending positions in the count) method so that the substring position is counted only in that range. Hence, the other form of count() method is: 
For example, we want to search for substring Delhi' in the main string New Delhi' to know how many times the substring appeared in the main string. We can use count() method as: str = 'New Delhi" 
stringname.count (substring, beg, end) 
n = str.count('Delhi') print (n) The output of the preceding statements is as follows: 1 Suppose, we want to know how many times 'e' is repeated in the main string in the range from 0th to 2nd characters, we can write: n = str.count('e', 0, 3) print(n) The output of the preceding statements is as follows: 1 
Strings and Characters 219 
If we search for 'e' in the main string starting from 0th character to the end of the string, we can write: n = str.count('e', 0, len(str)) print(n) The output of the preceding statements is as follows: 2 
Strings are Immutable An immutable object is an object whose content cannot be changed. On the other hand, a mutable object is an object whose content can be changed as and when required. In ython, numbers, strings and tuples are immutable. Lists, sets, dictionaries are mutable objects. There are two reasons why string objects are made immutable in Python. Performance: When an object is immutable, it will have fixed size in memory since it cannot be modified. Because strings are immutable, we can easily allocate memory space for them at creation time, and the storage requirements are fixed and unchanging. Hence it takes less time to allocate memory for strings and less time to access them. This increases the performance of the software. 

## Page 14
220 Chapter 8 Security: Since string objects are immutable, any attempts to modify the existing string object will create a new object in memory. Thus the identity number of thhe new object will change that lets the programmer to understand that somebody modified the original string. This is useful to enforce security where strings can be transported from one application to another application without modifications. In the following code, we create a string 'str' where we stored 4 characters: 'abcd'. Wher we display 0m character, i.e. str/0|, it will display 'a'. If we try to replace the 0th characte: with a new character x, then there will be an error called TypeError. This is a prot that strings are immutable. str = 'abcd' print(str[0]) 
as: 
str[0] ='x' Traceback (most recent call last): 
's2, as: We will take an ambiguous example. In this example, we are creating two strings 'sl' and TypeError: 'str object does not support item assignment File "<pyshell#7>", line 1, in <module str[0] = 'x' 
sl='one s2= two Now, we are modifying the content of the string 's2' by storing the content of 's1' into it S2 = S1 # store s1 into s2 If we display, the 's2' string, we can see the same content of 's1'. print (s2) # display s2 The output of the preceding statement is as follows: one If you write, print(s1) 
one Then, the output of the preceding statement is as follows: # display s1 
It seems that the content of 's2' is replaced by the content of 'sl' and hence 's2 beca mutable. But this is wrong, When we write: s2 = Sl The name 's2 will be adjusted to refer to the object that is referenced by 'sl: buL original value of 's2 that is two' is not altered. Since two' is not referenced, the gabes collector deletes that object from memory. Figure 8.2 shows the immutability of Striib objects: 

## Page 15
Sl='one' s2=two id(s1) 50848256 id(s2) 50848000 s2 = s1 id(s1) 50848256 id(s2) 50848256 
s1 = 'one' s2 = 'two' 
s2 = s1 
Identity number of an object internally refers to the memory address of the object and is given by id) function. If we display identity numbers using id) function, we can find that the identity number of 's2' and 's1' are same since they refer to one and the same object. 
stringname.replace(old, new) 
s2 = 
one 
s1 
Replacing a String with another String 
s1 1ower' 
one 
print (str) 
s2 Figure 8.2: Immutability of String Objects 
str = That is a beautiful gir]" strl = str.replace (s1, s2) 
Observe that the identity number of 's2' is changed after its modification, since it is referencing to a new object. 
Strings and Characters 221 
The replace() method is useful to replace a sub string in a string with another sub string. The format of using this method is: 
two 
That is a beautiful girl 
This will replace all the occurrences of old' sub string with new' sub string in the main string. For example, 
1 s2 
two 
The output of the preceding statement is as follows: 
If we display the contents of 'str' and 'strl', we can understand that the original string ´str' is not modified. Consider the following statement: 

## Page 16
222 Chapter 8 lf you write, print(str1) The output of the preceding statement is as follows: That is a beautiful flower 
Splitting and Joining Strings The split) meth0d is used to brake a string int0 pieces. These pieces are returned as list. For example, to brake the string 'str' where a comnma (, ) is found, we can write: str.split(', ") Observe the comma inside the parentheses. It is called separator that represents where to separate or cut the string. Similarly, the separator will be a space if we want to cut the string at spaces. In the following example, we are cutting the string 'str' wherever a comma is found. The resultant string is stored in 'str1' which is a list. str = 'one, two, three, four' strl = str.split(',) print(strl) The output of the preceding statements is as follows: ['one' two 'three' In Program 8, we are accepting a group of numbers as a string from the user. The numbers should be entered with space as separator. The numbers are stored by input) function into a string 'str' which is split into pieces where a space is found. The group ot numbers are stored into a list lst' from where we display them using a for loop. Paom Program 8: A Python program to accept and display a group of numbers. # to accept a group of numbers and display them. str = input('Eñter numbers separated by space: ') # cut the stri ng where a space is found 1st = str.split(') 
'four'] 
# display the numbers from the list for i in lst: print(i) Output: C:\>python str.py Enter numbers separated by space: 10 20 30 40 10 20 30 40 

## Page 17
When a group of strings are given, it is possible to join them all and make a single string. For this purpose, we can use join) method as: separator.join(str) where, the 'separator' represents the character to be used between the strings in the output. 'str' represents a tuple or list of strings. In the following example, we are taking a tuple 'str' that contains 3 strings as: str = ('one', 'two', 'three') We want to join the three strings and form a single string. Also, we want to use hyphen (-) between the three strings in the output. The join() method can be written as: strl = "-" print(strl)` join(str) The output of the preceding statemnents is as follows: one-tWo-three 
Sep = 
In the following example, we are taking a list comprising 4 strings and we are joining them using a colon (:) between them. Str = 'apple', 'guava', 'grapes', 'mango'] strl = sep.join(str) print (str1) The output of the preceding statements is as follows: 
# the output string is strl. 
apple:guava:grapes:mango Changing Case of a String 
Strings and Characters 223 
Python offers 4 methods that are useful to change the case of a string. They are upper), lower), swapcase(), title(). The upper) method is used to convert all the characters of a string into uppercase or capital letters. The lower() method converts the string into lowercase or into small letters. The swapcase() method converts the capital letters into Small letters and vice versa. The title() method converts the string such that each word in the string will start with a capital letter and remaining will be small letters. See the following examples: str = 'Python is the future' print(str.upper0) The output of the preceding statements is as follows: PYTHON IS THE FUTURE If you write, print(str. lower(O) Then, the output will be: python is the future 

## Page 18
224 Chapter 8 If you write, print(str.swapcase()) Then, the output will be: pYTHON IS THE FUTURE If you write the following statement: print (str.title(0) Then, the output will be: Python Is The Future Checking Starting and Ending of a String The startswith) method is useful to know whether a string is starting with a sub string or not. The way to use this method is: str.startswi th (substring) When the sub string is found in the main string 'str', this method returns True. If the sub string is not found, it returns False. Consider the following statements: str = This is Python' print(str.startswith('This')) The output will be: True Simlarly, to check the ending of a string, we can use endswith) method. It returns True if the string ends with the specified sub string, otherwise it returns False. str. endswi th(substring) str = This is Python print (str.endswi th('Python')) The output of the preceding statements is as follows: True 
String Testing Methods There are several methods to test the nature of characters in a string. These methods return either True or False. For example, if a string has only numeric digits, then 1saig 
Method 
method returns True. These methods can also be applied to individual characters. Table 8.2 mentioned the string and character testing methods: Table 8.2: String and Character Testing Methods isalnum() Description Ihis method returns True if all characters in the string alphanumeric (A to Z, a to z. 0 to 9) and there is at least one chart otherwise it returns False. 
