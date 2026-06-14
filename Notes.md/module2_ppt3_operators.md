# Lecture/Document: module2_ppt3_operators

## Page 1
UNIT 2: OPERATORS
Prachi Surlakar
Assistant Professor
Computer Engineering Department
Goa College of  Engineering


## Page 3
OPERATORS IN PYTHON
OPERATOR: Operator is a symbol that performs an operation.
 Example:  a + b
       ‘+’  : operator        a, b : operands
• Unary operator: Operator acts on a single variable.   
• Binary operator: Operator works on two variables.
• Ternary operator: Operator works on three variables.
We can classify operators as:
1. Arithmetic operators
2. Assignment operators
3. Unary minus operators
4. Relational operators
5. Logical operators
6. Boolean operators
7. Bitwise operators 
8. Membership operators
9. Identity operators


## Page 4
1. ARITHMETIC OPERATORS
Also called as binary operators. 
Assume a=13, b=5


## Page 5
1. ARITHMETIC OPERATORS
Precedence:
1. Parentheses
2. Exponentiation
3. Multiplication, division, modulus, floor division
4. Addition, subtraction
5. Assignment operation
Example:
   d=(x+y) *z** a//b +c      
 ( Assume x=1, y=2, z=3, a=2, b=2, c=3)
  d= (1+2) *3 ** 2 // 2+ 3
  d= 3 *3 ** 2 // 2+ 3
  d= 3 *9// 2+ 3
  d= 27// 2+ 3
  d= 13+ 3
  d=16
Example:
d=3**2//2+3
print(d)
Output:7
d=3**2//2+3
d=9//2+3
d=4+3
d= 7


## Page 6
Using python interpreter as calculator
1. ARITHMETIC OPERATORS


## Page 7
• Store right side value into a left side variable.
• Can also be used to perform simple arithmetic operations like addition, subtraction etc.
• Assume x=20 and y=10 z=5
2. ASSIGNMENT OPERATORS


## Page 8
• Store right side value into a left side variable.
• Can also be used to perform simple arithmetic operations like addition, subtraction etc.
• Assume x=20 and y=10 , z=5
2. ASSIGNMENT OPERATORS


## Page 9
2. ASSIGNMENT OPERATORS
Python does not have increment operator(++) and decrement operator(--)


## Page 10
3. UNARY MINUS OPERATOR
• Denoted by symbol minus(-)
• If  the variable value is positive it is converted to negative and vice versa.


## Page 11
4. RELATIONAL OPERATORS
These operators will return either true or false. Assume a=1 and b=2 


## Page 12
4. RELATIONAL OPERATORS
• Mostly used to construct conditions.
OUTPUT: No
If  we get all true then only final result 
will be true. If  any comparisons yields 
false, then we get false as the final result.


## Page 13
5.  LOGICAL OPERATORS
• Construct compound conditions.
• False:0 
• True: any other number.
 Consider x=1 and y=2 
1 and 2  =2
0 and 2 =0
1 or 2 =1
0 or 2 = 2
not 2= False
not 0 =True
Note: use print to display the output.


## Page 14
5.  LOGICAL OPERATORS
OUTPUT: ‘Yes’
When ‘and’ is used, total condition will 
be true only if  both conditions are true.
OUTPUT: ‘Yes’
When ‘or’ is used, if  any one condition 
is true it will take total compound 
condition as true..


## Page 15
6.BOOLEAN OPERATORS
• There are two ‘bool’ type literals. They are ‘True’ and ‘False’
Example : x=True  y=False 


## Page 16
6.BOOLEAN OPERATORS


## Page 17
7. BITWISE OPERATORS
• Bitwise operators act on individual bits (0 and 1) of  the operands.
• We can use bitwise operators directly on binary numbers or on integers also.
• When we use these operators on integers, these numbers are converted into bits(binary 
number system) and then bitwise operators act upon those bits.
• Results are in the form of  integers
• Decimal number system : consists numbers from 0 to 9.
• Binary number system: there are only 2 digits ( 0 and 1)
• There are six types of  bitwise operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator (<<)
5. Bitwise Right shift operator (>>)
6. Bitwise complement operator (~)


## Page 18
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator 
(<<)
5. Bitwise Right shift operator 
(>>)
6. Bitwise complement operator 
(~)


## Page 19
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
First convert 13 to binary
2 13 1
6


## Page 20
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
First convert 13 to binary
2 13 1
2 6 0
3


## Page 21
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
First convert 13 to binary
2 13 1
2 6 0
2 3 1
1


## Page 22
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
First convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0


## Page 23
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
First convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1


## Page 24
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
7
convert 14 to binary


## Page 25
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
3
convert 14 to binary


## Page 26
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
2 3 1
1
convert 14 to binary


## Page 27
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
2 3 1
2 1 1
0
convert 14 to binary


## Page 28
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
2 3 1
2 1 1
0
convert 14 to binary


## Page 29
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
2 3 1
2 1 1
0
convert 14 to binary
Write in 8 bits
14  = 0 0 0 0 1 1 1 0


## Page 30
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
2 3 1
2 1 1
0
convert 14 to binary
Write in 8 bits
14  = 0 0 0 0 1 1 1 0
13 & 14
13  = 0 0 0 0 1 1 0 1
14  = 0 0 0 0 1 1 1 0
         0 0 0 0 1 1 0 0


## Page 31
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
13 & 14
convert 13 to binary
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
convert 14 to binary
Write in 8 bits
14  = 0 0 0 0 1 1 1 0
13 & 14
13  = 0 0 0 0 1 1 0 1
14  = 0 0 0 0 1 1 1 0
         0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0  → convert to decimal
0 0 0 0 1 1 0 0
27 26 25 24 23 22 21 20
=0 * 20 + 0 * 21 +1 * 22 +1 * 23 +0 * 24 +0 * 25 +0 * 26 + 0 * 27
=0+0+4+8+0+0+0+0
=12 13 & 14 = 12


## Page 32
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
&(BITWISE AND) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying AND is 1 if  both are 1 otherwise 0
A B A&B
0 0 0
0 1 0
1 0 0
1 1 1
5 & 3
convert 5 to binary
2 5 1
2 2 0
2 1 1
0
Write in 8 bits
5 = 0 0 0 0 0 1 0 1
2 3 1
2 1 1
0
convert 3 to binary
Write in 8 bits
3  = 0 0 0 0 0 0 1 1
5 & 3
  5 = 0 0 0 0 0 1 0 1
  3 = 0 0 0 0 0 0 1 1
         0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 1→ convert to decimal
0 0 0 0 0 0 0 1
27 26 25 24 23 22 21 20
=1 * 20 + 0 * 21 +0 * 22 +0 * 23 +0 * 24 +0 * 25 +0 * 26 + 0 * 27
=1+0+0+0+0+0+0+0
=1 5 & 3 = 1


## Page 33
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
|(BITWISE OR) OPERATOR
• Every number will be stored in the form of  bits(0s and 1s)
• Result of  applying OR is 1 if  at least one bit value is ‘1’ otherwise ‘0’
A B A|B
0 0 0
0 1 1
1 0 1
1 1 1
13 | 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
2 3 1
2 1 1
0
convert 14 to binary
Write in 8 bits
14  = 0 0 0 0 1 1 1 0
13 | 14
13  = 0 0 0 0 1 1 0 1
14  = 0 0 0 0 1 1 1 0
         0 0 0 0 1 1 1 1
0 0 0 0 1 1 1 1  → convert to decimal
0 0 0 0 1 1 1 1
27 26 25 24 23 22 21 20
=1 * 20 + 1 * 21 +1 * 22 +1 * 23 +0 * 24 +0 * 25 +0 * 26 + 0 * 27
=1+2+4+8+0+0+0+0
 =15 13 | 14 = 15
BITWISE OR
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator
5. Bitwise Right shift operator
6. Bitwise complement operator 


## Page 34
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
^(BITWISE XOR) OPERATOR
• Result of  applying XOR is 1 if  ONLY one bit value is ‘1’ otherwise ‘0’
A B A^B
0 0 0
0 1 1
1 0 1
1 1 0
13 ^ 14
convert 13 to binary
2 13 1
2 6 0
2 3 1
2 1 1
0
Write in 8 bits
13  = 0 0 0 0 1 1 0 1
2 14 0
2 7 1
2 3 1
2 1 1
0
convert 14 to binary
Write in 8 bits
14  = 0 0 0 0 1 1 1 0
13 ^ 14
13  = 0 0 0 0 1 1 0 1
14  = 0 0 0 0 1 1 1 0
         0 0 0 0 0 0 1 1
0 0 0 0 0 0 1 1  → convert to decimal
0 0 0 0 0 0 1 1
27 26 25 24 23 22 21 20
=1 * 20 + 1 * 21 +0 * 22 +0 * 23 
+0 * 24 +0 * 25 +0 * 26 + 0 * 27
=1+2+0+0+0+0+0+0
=3
13 ^ 14 = 3
BITWISE XOR
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator
5. Bitwise Right shift operator
6. Bitwise complement operator 


## Page 35
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
Write the output of  the following
OUTPUT:


## Page 36
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
<< Left shift operator
Shifts bit to the left
a=10, perform a<<1 and a<<2
2 10 0
2 5 1
2 2 0
2 1 1
0
Convert 10 to binary
a=10  = 0 0 0 0 1 0 1 0
a<<1 
0 0 0 0 1 0 1 0
0 0 0 1 0 1 0 0   
0 0 0 1 0 1 0 0
27 26 25 24 23 22 21 20
=0 * 20 + 0 * 21 +1 * 22 +0 * 23 +1 * 24 
+0 * 25 +0 * 26 + 0 * 27
=0+0+4+0+16+0+0+0 =20
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator
5. Bitwise Right shift operator
6. Bitwise complement operator 


## Page 37
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
<< Left shift operator
Shifts bit to the left
a=10, perform a<<1 and a<<2
2 10 0
2 5 1
2 2 0
2 1 1
0
Convert 10 to binary
a=10  = 0 0 0 0 1 0 1 0
a<<1 
0 0 0 0 1 0 1 0
0 0 0 1 0 1 0 0   
a<<2 
0 0 0 0 1 0 1 0
0 0 1 0 1 0 0 0
0 0 0 1 0 1 0 0
27 26 25 24 23 22 21 20
=0 * 20 + 0 * 21 +1 * 22 +0 * 23 +1 * 24 
+0 * 25 +0 * 26 + 0 * 27
=0+0+4+0+16+0+0+0 =20
0 0 1 0 1 0 0 0
27 26 25 24 23 22 21 20
=0 * 20 + 0 * 21 +0 * 22 +1 * 23 
+0 * 24 +1 * 25 +0 * 26 + 0 * 27
=0+0+0+8+0+32+0+0 
=40
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator
5. Bitwise Right shift operator
6. Bitwise complement operator 


## Page 38
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
>> Right shift operator
Shifts bit to the right
a=10, perform a>>1 and a>>2
2 10 0
2 5 1
2 2 0
2 1 1
0
Convert 10 to binary
a=10  = 0 0 0 0 1 0 1 0
a>>1 
0 0 0 0 1 0 1 0
0 0 0 0 0 1 0 1   
0 0 0 0 0 1 0 1
27 26 25 24 23 22 21 20
=1 * 20 + 0 * 21 +1 * 22 +0 * 23 +0 * 24 +0 * 25 +0 * 26 + 0 * 27
=1+0+4+0+0+0+0+0 =5
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator
5. Bitwise Right shift operator
6. Bitwise complement operator 


## Page 39
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
>> Right shift operator
Shifts bit to the right
a=10, perform a>>1 and a>>2
2 10 0
2 5 1
2 2 0
2 1 1
0
Convert 10 to binary
a=10  = 0 0 0 0 1 0 1 0
a>>1 
0 0 0 0 1 0 1 0
0 0 0 0 0 1 0 1   
a>>2 
0 0 0 0 1 0 1 0
0 0 0 0 0 0 1 0
0 0 0 0 0 1 0 1
27 26 25 24 23 22 21 20
=1 * 20 + 0 * 21 +1 * 22 +0 * 23 +0 * 24 
+0 * 25 +0 * 26 + 0 * 27
=1+0+4+0+0+0+0+0 =5
0 0 0 0 0 0 1 0
27 26 25 24 23 22 21 20
=0 * 20 + 1 * 21 +0 * 22 +0 * 23 +0 * 
24 +0 * 25 +0 * 26 + 0 * 27
=0+2+0+0+0+0+0+0
 =2
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator
5. Bitwise Right shift operator
6. Bitwise complement operator 


## Page 40
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
Find the output of  the following code
Output:


## Page 41
7.  BITWISE OPERATOR
BITWISE OPERATORS
  
~ Ones complement
All 1s are changed to 0s and 0s to 1s
Example:
Find ones complement of  0010
0 0 1 0
1 1 0 1
Example:
Find ones complement of  2
2 2 0
2 1 1
0
Convert 2 to binary
2    0 0 0 0 0 0 1 0
~2    1 1 1 1 1 1 0 1
• There are six types of  bitwise 
operators:
1. Bitwise AND operator (&)
2. Bitwise OR operator ( | )
3. Bitwise XOR operator (^)
4. Bitwise Left shift operator
5. Bitwise Right shift operator
6. Bitwise complement operator 
Convert back to decimal


## Page 42
7.  BITWISE OPERATOR


## Page 43
Determine the output of  the following program
OUTPUT


## Page 44
There are two membership 
operators.
• in
• not in
8. MEMBERSHIP OPERATORS in Operator
The in operator returns True if  the specified element is 
present in the sequence; otherwise, it returns False.
not in Operator
The not in operator returns True if  the specified element is 
not present in the sequence; otherwise, it returns False.


## Page 45
There are two membership 
operators.
• in
• not in
8. MEMBERSHIP OPERATORS
If  we want to display the members of  the list using for 
loop we use the ‘in’ operator.
When true is returned the print( ) function in the for 
loop is executed and the name is displayed.


## Page 46
There are two identity 
operators.
• is
• is not
9. IDENTITY OPERATORS • These operators compare the memory locations of  two 
objects. Hence it is possible to know whether the two objects 
are same or not.
• Memory location of  an object can be seen using the id( ) 
function.
Example:
Here 25 is the object for which two names 
are given. If  we display identity number  we 
get the same numbers as they refer to the 
same object.
# Example with numbers
a = 25
b = 25
print(a is b)     # Output: True
print(a is not b) # Output: False


## Page 47
There are two identity 
operators.
• is
• is not
9. IDENTITY OPERATORS 1. The is operator
• The is operator is used to compare whether two objects 
are same or not.
• It will internally compare the identity number of  the 
objects.
• If  identity numbers of  the objects are same, it will return 
True or else it returns false
2. The is not operator
• Is not operator returns true if  identity numbers of  two 
objects being compared are not the same. If  they are 
same it will return false.
The is and is not operators do not compare the values of  the 
objects.
 They compare the identity numbers or memory locations of  the 
objects.


## Page 48
Program:
Output:
9. IDENTITY OPERATORS
Program:
Output:
‘is’ operator does not compare the values. It 
compares the identity numbers of  the lists.
Both lists are stored at 
different memory 
locations.


## Page 49
9. IDENTITY OPERATORS
We can use equality operator(==) to compare the values.
OUTPUT:


## Page 50
OPERATOR PRECEDENCE AND ASSOCIATIVITY


## Page 51
OPERATOR PRECEDENCE AND ASSOCIATIVITY
Associativity
• Associativity is the order in which  an expression is evaluated that has multiple 
operators of  same precedence.  


## Page 52
MATHEMATICAL FUNCTIONS
• A module is a file that contains group of  useful objects like functions, classes or variables.
• ‘math’ is a module that contains several functions to perform mathematical operations.
• If  we want to use any module in our python program, first we should import that module 
into our program by writing ‘import’ statement.
• To import math module we can write
Method 1:
import math
x=math.sqrt(16)
Method 2:
import math as m
x=m.sqrt(16)
Method 3:
from math import sqrt
x=sqrt(16)
Method 3:
from math import factorial, sqrt
x=sqrt(16)
y=factorial(5)
Note: These functions cannot be used with 
complex  numbers. To use functions with 
complex numbers separate module called 
‘cmath’ is used.


## Page 53
MATHEMATICAL FUNCTIONS


## Page 54
MATHEMATICAL FUNCTIONS


## Page 55
MATHEMATICAL FUNCTIONS


## Page 56
MATHEMATICAL FUNCTIONS


## Page 57
MATHEMATICAL FUNCTIONS


## Page 58
MATHEMATICAL FUNCTIONS
Write a python program to calculate area of  a circle.( Use mathematical constant pi)


## Page 59
THANK YOU☺
by PRACHI SURLAKAR

