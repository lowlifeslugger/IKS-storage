# Lecture/Document: mod4_PPT1

## Page 1
UNIT 4: FUNCTIONS
LIST AND TUPLES
Prachi Surlakar
Assistant Professor
Computer Engineering Department
Goa College of  Engineering


## Page 3
FUNCTIONS
• A function consists of  a group of  statements that are intended to perform a specific task.
• Built in ( ) functions: print( ), sqrt ( ), etc.
• User defined functions:  Functions created by the programmer.
• Advantages of  functions:
❖ Functions are used to process data, make calculations, or perform any task which is 
required for software development.
❖ Once function is written it can be reused as and when required.
❖ Provide modularity for programming.
❖ Code maintenance is easy.
❖ When there is error corresponding function can be modified.
❖ Use of  functions will reduce length of  a program.


## Page 4
DIFFERENCE BETWEEN FUNCTION AND A METHOD
• A function can be written individually in a python program.
• A function is called using its name.
• When a function is written inside a class, it becomes a method.
• A method is called using the following ways.
• So a function and a method are same except their placement and the way they are called.


## Page 5
DEFINING A FUNCTION
• We can define a function using the def  keyword followed by function name.
• After the function name we should write parenthesis( )
Function definition:
Example:
• Parameter: is a variable that receives data from outside into a function.
• After parenthesis we put a colon(:) that represents the beginning of  a function.
• Function body contains a group of  statements called suite.
• Docstring : Optional. Gives information about the function.


## Page 6
CALLING A FUNCTION
• A function cannot run on its own. It runs only when we call it. We have to call the function using 
its name.
Write a function that finds the sum of  two numbers
OUTPUT:
Dynamic typing: Type of  the data is determined only during runtime


## Page 7
RETURNING RESULTS FROM A FUNCTION
• We can return the result or the output from the function using the return statement. 
Write a python program to find the sum of  two numbers and return the result from the function
OUTPUT:


## Page 8
Write a python program to check if  a number is even or odd using functions.
OUTPUT:


## Page 9
RETURNING RESULTS FROM A FUNCTION
Write a python program to find factorial of  numbers from 1 to 10 using functions
EXPLANATION


## Page 10
RETURNING RESULTS FROM A FUNCTION
Write a python program to find factorial of  numbers from 1 to 10 using functions
OUTPUT


## Page 11
Write a program using functions to check if  a given number is prime or not
Example 1:
n= 5
For i in range(2,5) – values 2,3,4
5%2==0
5%3==0
5%4==0
x=1
return 1 
Print 5 is prime
Example 2:
n= 4
For i in range(2,4) – values 2,3
4%2==0
x=0 break
return 0
Print 4 is not prime
OUTPUT:
RETURNING RESULTS FROM A FUNCTION:


## Page 12
Write a program to check if  a given number is prime or not
Example 1:
n= 5
For i in range(2,5) – values 2,3,4
5%2==0
5%3==0
5%4==0
x=1
return 1 
Print 5 is prime
Example 2:
n= 4
For i in range(2,4) – values 2,3
4%2==0
x=0 break
return 0
Print 4 is not prime
OUTPUT:


## Page 13
RETURNING MULTIPLE VALUES FROM A FUNCTION
• Function can return multiple values in python.
• Example: return a, b, c
• Values are returned by a function as a tuple.
Write a python program to show how a function returns multiple values.
OUTPUT:


## Page 14
RETURNING MULTIPLE VALUES FROM A FUNCTION
Write a python function that returns multiple values of  addition, subtraction, multiplication and 
division
CODE: OUTPUT:


## Page 15
FORMAL AND ACTUAL ARGUMENTS
Formal arguments: When a function is defined, it may have some parameters. These parameters are 
useful to receive values from outside the function.
Actual arguments: When we call the function we should pass data or values to the function. These 
values are called actual arguments.


## Page 16
The actual arguments are of  4 
types:
1. Positional arguments.
2. Keyword arguments.
3. Default arguments.
4. Variable length arguments 
Positional Arguments
ACTUAL ARGUMENTS
• Number of  arguments and their positions in the function 
definition should match exactly with the number and 
position of  argument in the function call.
Python program to understand positional arguments
OUTPUT:


## Page 17
The actual arguments are of  4 
types:
1. Positional arguments.
2. Keyword arguments.
3. Default arguments.
4. Variable length arguments 
keyword Arguments
ACTUAL ARGUMENTS
• Arguments that identify the parameters by their names.
Python program to understand keyword arguments
OUTPUT:


## Page 18
The actual arguments are of  4 
types:
1. Positional arguments.
2. Keyword arguments.
3. Default arguments.
4. Variable length arguments 
Default Arguments
ACTUAL ARGUMENTS
• Default argument: is an argument that assumes a default value 
if  a value is not provided in the function call for that 
argument.
Python program to understand default arguments
OUTPUT:


## Page 19
The actual arguments are of  4 
types:
1. Positional arguments.
2. Keyword arguments.
3. Default arguments.
4. Variable length arguments 
Variable length ArgumentsACTUAL ARGUMENTS
• Sometimes programmer 
cannot decide how many 
arguments to be given in 
function definition.
• If  the programmer wants to 
develop a function that can 
accept n arguments then a 
variable length argument is 
used in function definition.
• Variable length argument is 
written with a ‘ * ’ symbol.
Python program to show variable length argument and its use
OUTPUT:


## Page 20
The actual arguments are of  4 
types:
1. Positional arguments.
2. Keyword arguments.
3. Default arguments.
4. Variable length arguments 
Variable length ArgumentsACTUAL ARGUMENTS
• Keyword variable length 
argument is an argument 
that can accept any number 
of  values provided in the 
format of  keys and values.
• Declare it with a ‘ ** ’ before 
the argument. 
OUTPUT:
Write a python program to understand keyword variable argument


## Page 21
LOCAL AND GLOBAL VARIABLES
• Local variable: declared inside a function. Scope is limited only to 
that function where it is created. 
• Global variable: Scope of  the global variable is the entire program 
body written below it.
When local and global variables have the same name, 
function by default refers the local variable.


## Page 22
PASSING A GROUP OF ELEMENTS TO A FUNCTION
To pass a group of  elements like numbers or strings, we can accept them into a list and then pass 
the list to the function where the required processing can be done.
Write a function to accept a group of  numbers and find their total and average
OUTPUT


## Page 23
PASSING A GROUP OF ELEMENTS TO A FUNCTION
Write a function to display a group of  strings
OUTPUT:


## Page 25
LIST
• List can store a group of  elements.
• Can store different types of  elements.
• More versatile and useful than array.
To create an empty list
Create a list to store student information
Print student list
Print student name


## Page 26
LIST
Slicing operations on lists:
Format: [start : stop : step size]
By default start will be zero and stop will be the last element and step size will be 1 
CODE: OUTPUT:


## Page 27
LIST
Write a python program to create a list with different types of  elements.
OUTPUT:


## Page 28
Creating lists using range( ) function
Write a python program to create following lists using range function
• List of  numbers from 0 to 4
• List of  numbers from 2 to 4
• Odd numbers from 5 to 10
 OUTPUT:


## Page 29
Write a python program to access elements of  a list using while and for loops. 
OUTPUT:


## Page 30
UPDATING ELEMENTS OF A LIST
Lists are mutable. We can modify the contents of  a list.
Create a list
Append elements to a list
Update second element of  a list


## Page 31
UPDATING ELEMENTS OF A LIST
Update second and third element
Delete elements
Reverse elements of  a list
OUTPUT:


## Page 32
Perform the following operations on lists
• Create a list with elements from 0 to 9
• Append value 10 to the list
• Update the fourth element of  the list to 40.
• Update the second and third element of  a list to 20 and 30 respectively.
• Delete first element of  the list.
• Reverse the list elements.


## Page 33
UPDATING ELEMENTS OF A LIST
Write a python program to display elements of  a list in reverse order
OUTPUT


## Page 34
CONCATENATION OF TWO LISTS
+ operator can be used on two lists to join them.
OUTPUT:


## Page 35
REPETITION OF LISTS
We can repeat elements of  a list ‘n’ number of  times using the ‘*’ operator.
OUTPUT:


## Page 36
METHODS TO PROCESS LISTS


## Page 37
Write a python program to understand the list 
processing methods


## Page 38
Write a python program to understand the list processing methods
OUTPUT:


## Page 39
FINDING BIGGEST AND SMALLEST ELEMENTS IN A LIST
max( ) and min( ) functions return the biggest and the smallest element from the list.


## Page 40
FINDING BIGGEST AND 
SMALLEST ELEMENTS IN A 
LIST without using max( ) and 
min( ) functions.


## Page 41
FINDING BIGGEST AND SMALLEST ELEMENTS IN A LIST without using max( ) and min( ) functions.


## Page 42
SORTING THE LIST ELEMENTS
sort( ) method: sorts elements of  a list.
Example:
x.sort( ) # sorts elements in list x in sorted order
x.sort(reverse=True) # sorts list x in descending order
SORTING WITHOUT USING THE SORT( ) METHOD
SWAPPING


## Page 43
OUTPUT


## Page 44
TUPLE
• Tuple stores a group of  elements or items.
• Tuples are immutable whereas lists are mutable.
• We cannot perform operations like append(), insert( ), remove( ), pop( ) and clear( ) on tuples.
• Tuples used to store data which should not be modified.
• We can create a tuple by writing elements inside parentheses ( )
Different ways of  creating tuples


## Page 45
TUPLE
Different ways of  creating tuples
OUTPUT:


## Page 46
ACCESSING THE TUPLE ELEMENTS


## Page 47
SLICING OPERATIONS ON TUPLES
[start: stop: stepsize]


## Page 48
BASIC OPERATIONS ON TUPLES
Len ( ): finds the length of  a tuple
Concatenate using the + operator
OUTPUT:
‘in’ and ‘not in’ operator


## Page 49
REPITITION OPERATOR
OUTPUT:


## Page 50
DIFFERENTIATE BETWEEN LISTS AND TUPLES


## Page 51
MORE PATTERNS IN PYTHON


## Page 54
THANK YOU☺
by PRACHI SURLAKAR

