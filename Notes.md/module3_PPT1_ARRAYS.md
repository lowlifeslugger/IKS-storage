# Lecture/Document: module3_PPT1_ARRAYS

## Page 1
UNIT 3: ARRAYS
Prachi Surlakar
Assistant Professor
Computer Engineering Department
Goa College of  Engineering
PRACHI SURLAKAR

## Page 2
PRACHI SURLAKAR

## Page 3
ARRAYS IN PYTHON
• Array is an object that stores a group of  elements of  same datatype.
• Arrays can store only one type of  data.
• Arrays can increase or decrease their size dynamically.
Advantages of  arrays
• Arrays use less memory than lists and they offer faster execution than lists.
• No need to specify how many elements we are going to store into an array in the 
beginning.
• Arrays can grow or shrink in memory dynamically.
• Methods that are useful to process the elements of  any array are available in array 
module
PRACHI SURLAKAR

## Page 4
ARRAYS IN PYTHON
Creating an Array:
arr=array(‘f ’, [1.5 ,-2.2 ,3 6.75]
Examples:
a= array(‘ i ’,[4, 6, 2, 9])
PRACHI SURLAKAR

## Page 5
IMPORTING THE ARRAY MODULE
There are three ways  to import the array module into our program.
Method 1:
import array
a= array.array(‘i’,[4,6,2,9])
# here first ‘array’ represents the module name and next array represents the class name.
method 2:
import array as ar
a= ar.array(‘i’,[4,6,2,9])
Method 3:
from array import *
a=array (‘i’,[4,6,2,9])
# * symbol represents all. The meaning is it imports all classes, objects, variables etc, from 
array module into our program.
PRACHI SURLAKAR

## Page 6
IMPORTING THE ARRAY MODULE
1. Write a python program to create an integer type array and display those elements
Output:
Method 1: Method 2:
Output:
PRACHI SURLAKAR

## Page 7
IMPORTING THE ARRAY MODULE
2. Write a python program to create an array with a group of  characters.
Output:
PRACHI SURLAKAR

## Page 8
IMPORTING THE ARRAY MODULE
3. Create an array named as ‘arr1’ with elements as 10,20,30,40.  Create another array named 
‘arr2’ by multiplying the elements of  the first array by five. Print the elements of  the ‘arr2’ 
array.
Output:
PRACHI SURLAKAR

## Page 9
INDEXING AND SLICING ON ARRAYS
Index: index represents the position number of  an element in an array.
Example:
x=array ( ‘i’ ,[ 10, 20, 30, 40, 50] )
Elements are stored as:
PRACHI SURLAKAR

## Page 10
INDEXING AND SLICING ON ARRAYS
4. Write a python program to retrieve the elements of  an array using array index
i print
0 x[0]=10
1 x[1]=20
2 x[2]=30
3 x[3]=40
0 x[4]=50
n=5
for i in range(5) #0 to 4
Explanation:
PRACHI SURLAKAR

## Page 11
INDEXING AND SLICING ON ARRAYS
Slicing operations: is used to retrieve a piece of  the array that contains a group of  elements.
Syntax:
arrayname(start: stop: stride)
Stride: step size excluding the starting element, optional.
PRACHI SURLAKAR

## Page 12
SLICING ON ARRAYS
10 20 30 40 50 60 70
x[0] x[1] x[2] x[3] x[4] x[5] x[6]
x[-7] x[-6] x[-5] x[-4] x[-3] x[-2] x[-1]
OUTPUT:
PRACHI SURLAKAR

## Page 13
SLICING ON ARRAYS
10 20 30 40 50 60 70
x[0] x[1] x[2] x[3] x[4] x[5] x[6]
x[-7] x[-6] x[-5] x[-4] x[-3] x[-2] x[-1]
OUTPUT:
PRACHI SURLAKAR

## Page 14
INDEXING AND SLICING ON ARRAYS
Slicing : can be used to create new arrays from existing arrays.
Slicing can be used to update an array.
OUTPUT:
PRACHI SURLAKAR

## Page 15
INDEXING AND SLICING ON ARRAYS
Write a python program to retrieve and display only a range of  elements from an array using slicing.
OUTPUT:
PRACHI SURLAKAR

## Page 16
Determine the output of  the following code
OUTPUT:
PRACHI SURLAKAR

## Page 17
PROCESSING THE ARRAYS
PRACHI SURLAKAR

## Page 18
PROCESSING THE ARRAYS
 Write a python program to understand the different methods of  arrays
PRACHI SURLAKAR

## Page 19
PROCESSING THE ARRAYS
OUTPUT:
PRACHI SURLAKAR

## Page 20
PROCESSING THE ARRAYS
Write a python program to store students marks into an array and find total marks and percentage of  marks.
OUTPUT:
PRACHI SURLAKAR

## Page 21
Write a program to sort elements of  the array using bubble sort technique.
Bubble sort example
PRACHI SURLAKAR

## Page 22
Write a program to sort elements 
of  the array using bubble sort 
technique.
PRACHI SURLAKAR

## Page 23
OUTPUT:
PRACHI SURLAKAR

## Page 24
Write a program to search for the position of  an element in an array using sequential search
PRACHI SURLAKAR

## Page 25
Write a program to search for the position of  an element in an array using sequential search
PRACHI SURLAKAR

## Page 26
Write a program to search for the position of  an element in an array using sequential search
OUTPUT:
PRACHI SURLAKAR

## Page 27
Write a program to search for the position of  an element in an array using index( ) method
PRACHI SURLAKAR

## Page 28
Write a program to search for the position of  an element in an array using index( ) method
OUTPUT
PRACHI SURLAKAR

## Page 29
TYPES OF ARRAYS
SINGLE DIMENSIONAL ARRAYS:
• These arrays represent only one row or one column of  elements.
• Example:
     marks= array(‘i’, [50,60,70,66,72])
MULTIDIMENSIONAL ARRAYS: 
• These arrays represent more than one row and more than one column of  elements.
• A two dimensional array is a combination of  several  single dimensional arrays. A three 
dimensional array is a combination of  several two dimensional arrays.
• We can construct multi dimensional arrays using third party packages like 
numpy( numerical python).
PRACHI SURLAKAR

## Page 30
WORKING WITH ARRAYS USING NUMPY
• numpy is a package that contains several classes, functions, variables etc. to deal with 
scientific calculations in python.
• Create and process single and multi dimensional arrays.
• Contains large library of  mathematical functions like linear algebra functions and Fourier transforms.
• The arrays which are created using numpy are called n dimensional arrays where n can be any 
integer.
• If  n=1 it represents one dimensional array. If  n=2 it represents two dimensional array , if  n=3 
it represents three dimensional arrays.
• Three methods to work with numpy
• Method 1: import numpy
Python program to create single dimensional array using numpy
OUTPUT: PRACHI SURLAKAR

## Page 31
WORKING WITH ARRAYS USING NUMPY
• Method 2: import numpy as np
• Method 3: from numpy import *
PRACHI SURLAKAR

## Page 32
Creating arrays using array( )
When we create an array we can specify the datatype of  the element either as ‘int’ , ‘float’ or 
dtype=string.
# integer array. We can also eliminate int
# float array
#If  one element belongs to float type, then it will 
convert all other elements also to float type.
#create array with character type elements
arr= array([‘Delhi’ , ‘Goa’ , ‘ Mumbai’ , ‘Hyderabad’] , dtype=str)  #we can store a group of  strings
arr= array([‘Delhi’ , ‘Goa’ , ‘ Mumbai’ , ‘Hyderabad’])  #we can omit dtype=str 
PRACHI SURLAKAR

## Page 33
Creating arrays using array( )
Write a python program to create a string type array using numpy.
PRACHI SURLAKAR

## Page 34
Creating arrays using array( )
Write a python program to create an array from another array.
OUTPUT:
PRACHI SURLAKAR

## Page 35
MATHEMATICAL OPERATIONS ON ARRAYS
It is possible to perform various mathematical operations on the elements of  the array.
Example 1:
#
Example 2:
These kind of  operations are called as vectorized operations. Vectorized operations are 
important because:
• Vectorized operations are faster. 
• Vectorized operations are Syntactically clearer.
• Vectorized operations provide compact code.
PRACHI SURLAKAR

## Page 36
PRACHI SURLAKAR

## Page 37
PRACHI SURLAKAR

## Page 38
Python program to perform some mathematical operations on a numpy array
PRACHI SURLAKAR

## Page 39
Python program to perform some mathematical operations on a numpy array
PRACHI SURLAKAR

## Page 40
Python program to perform some mathematical operations on a numpy array
OUTPUT
PRACHI SURLAKAR

## Page 41
THANK YOU☺
by PRACHI SURLAKAR
PRACHI SURLAKAR
