# Lecture/Document: module2_ppt1_Introduction to python

## Page 1
UNIT 2: 
INTRODUCTION TO 
PYTHON
Prachi Surlakar
Assistant Professor
Computer Engineering Department
Goa College of  Engineering


## Page 3
INTRODUCTION TO PYTHON
• Python is a programming language that combines features of  C and Java
• C: elegant style of  developing programs 
• Java: Classes and objects like Java
• Python will have very few lines of  code compared to C and Java.
• Example: Python Program to add two numbers 
 
a=b=10  # take two variables and store 10 into them
print(“Sum= ”,(a+b)) #display their sum
• Few lines of  code and easy to understand
• Developed by Guido Van Rossum in 1991
• Open source software: anybody can freely download it


## Page 4
INTRODUCTION TO PYTHON : FEATURES OF PYTHON
❖ Simple: Python is a simple programming language. When we read a python program we feel 
like reading English sentences. Hence developing and understanding is easier.
❖ Easy to learn: Uses very few keywords. Simple structure. Resembles C language. 
Migrating from C to python is easy.
❖ Open source: No need to pay for python software. Python can be freely downloaded from 
www.python.org website.
❖ High level language: Programming languages are of  two types: low level and high level
    High level languages use English words to develop programs. Python is high level language.
❖ Dynamically typed: we do not declare anything. If  a name is assigned to an object of  one 
type, it may later be assigned to an object of  different type.
❖ Platform independent: Python programs are not dependent on any specific operating 
system. Python can be used on almost all operating systems like UNIX,Linux, Windows,Mac.
❖ Portable: Python programs yields the same result on any computer in the world as they are 
platform independent
❖ Procedure and object oriented: procedure oriented uses functions and procedures(eg: C)
      object oriented: uses classes and objects(eg: C++ and Java)


## Page 5
INTRODUCTION TO PYTHON : FEATURES OF PYTHON
❖ Interpreted: Python program is called source code. After writing python program we 
should compile the source code using python compiler.
❖ Extensible: Programs written in C and C++ can be integrated into python and executed 
using PVM(Python virtual machine)
❖ Embeddable: We can insert python programs into C or C++ programs.
❖ Huge library: Python has a big library which can be used on any operating systems
❖ Database connectivity: Python uses interfaces to connect its programs to all major 
databases.
❖ Scalable: Python programs are scalable since they can run on any platform and use 
features of  new platform
❖ Batteries included: Huge library of  python contains several small applications which are 
already developed and immediately available for programmers.
      numpy : is a package for processing arrays
      w3lib: is a package of  web related functions


## Page 6
EXECUTION OF A PYTHON PROGRAM
• We write a python program(source code) with the name x.py
• Compiler converts python program into byte code
• Byte code instructions are contained in the file x.pyc
• PVM converts byte code to machine code(0s and 1s) using interpreter.
• Machine code instructions are executed by processor and results displayed.
• Interpreter translates the program source line by line and hence slow.
• To rectify this problem sometimes a Just in time compiler is added to improve the speed.
• Source code→byte code→machine code→ output are internally completed and then 
the final result is displayed.


## Page 7
PYTHON VIRTUAL MACHINE
• Program source code→ byte code→ machine code  
• Byte code fixed set of  instructions representing all operations. Size of  each 
instruction is 1 byte.
• Byte code instructions are in .pyc file.
• Python virtual machine( PVM) converts byte code to machine code 
• PVM uses interpreter to convert byte code to machine code and sends machine 
code to computer processor for execution.


## Page 8
Memory management in python
• In C the programmer should allocate or deallocate memory dynamically( using functions 
like malloc( ) , free( ).
• In python memory allocation and deallocation are done automatically by python 
virtual machine(PVM).
• Everything is considered as an object in python.eg: strings , functions are objects.
• Memory manager inside PVM allocates memory required for objects created in a 
python program.
• Objects are stored in heap.
• Size of  the heap depends on the random access memory(RAM) of  our computer 
and can increase/decrease based on requirement of  the program.


## Page 9
Memory management in python
• Operating system: Memory(RAM) for any program is allocated by  the operating system.
• Raw memory allocator: oversees whether enough memory is available to it for storing objects.
• Object specific allocators: implement different types of  memory management policies depending 
on the type of  objects. E.g. integer number should be stored in memory in one way and a string should 
be stored in a different way.


## Page 10
Garbage collection in Python
• Garbage collector is a module in python that is useful to delete objects from memory, 
which are not used in the program.
• The module that represents the garbage collector is named as gc.
• Garbage collector is the simplest way to maintain count for each object regarding how 
many times the object is referenced(or used).
• When object has some count, garbage collector will not remove it from memory .
• When an object is found with reference count 0, it will be deleted from the memory .
• Garbage collector can detect reference cycles and remove objects in the cycle.


## Page 11
Garbage collection in Python
• Garbage collector classifies object into three generations.
• Newly created objects are considered as generation 0 objects.
• When garbage collector examines the object in memory and does remove an object from 
memory due(because it is used by a program) then that object is placed into the next 
generation that is generation 1.
• When garbage collector intends to delete the objects for the second time and the object 
survives for  the second time, then it is placed in generation 2. 
• Older objects belongs to generation 2.
• Garbage collector tries to delete younger objects which are not referenced in the program 
rather than the old objects.
• Garbage collector run automatically. Python schedules garbage collector depending on a 
number called as threshold.
• In some cases where reference cycles are found in the program, it is better to run the 
garbage collector manually.


## Page 12
COMPARISON BETWEEN C AND PYTHON
C PYTHON
C is a procedure oriented programming language. 
It does not contain features like classes , objects , 
inheritance etc.
Python is object oriented programming 
language. It contains features like classes objects 
inheritance, polymorphism etc.
C programs execute faster Slower as compared to C
It is compulsory to declare the datatypes of  
variables arrays etc in C
Type declaration is not required in python
C language type discipline is static and weak Python type discipline is dynamic and strong
Pointers concept is available in C Python does not use pointers.
C does not have exception handling Python handles exceptions and hence it is robust
C has do while, while and for loops Python has while and for loops


## Page 13
COMPARISON BETWEEN C AND PYTHON
C PYTHON
C has switch statement Python does not have switch statements
The variable in for loop does dot increment 
automatically.
Variable in for loop increments automatically
Programmer should allocate and deallocate 
memory using malloc( ), calloc( ), free( ) and 
realloc( )
Memory allocation and deallocation done by 
PVM
C supports single and multidimentional arrays Python supports only single dimentional arrays. 
To work with multidimentional arrays we should 
use third part applications like numpy
Array index should be a positive integer Array index can be positive or negative 
integer.Negative index represents locations from 
the end of  the array.
Indentation of  statements is not necessary in C Indentation is required to represent a block of  
statements
Semicolon is used to terminate the statements New line indicates end of  statements


## Page 14
COMPARISON BETWEEN JAVA AND PYTHON


## Page 17
THANK YOU☺
by PRACHI SURLAKAR

