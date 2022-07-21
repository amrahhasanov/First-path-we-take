#python 6
"""Task 1.
Import a packet of numpy, then use the array function to create two 3-element vectors
and perform the following operations on them, interpret the results:"""
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
#1) +
result1 = arr1 + arr2
print(result1)
#2) -
result2 = arr1 - arr2
print(result2)
#3) *
result3 = arr1 * arr2
print(result3)
#4) /
result4 = arr1 / arr2
print(result4)
#5) **
result5 = arr1 ** arr2
print(result5)
#6) %
result6 = arr2 % arr1
print(result6)

"""Task 2.
Using the matrix function, create two 3x3 arrays and perform the following operations on them, 
interpret the results:
"""
#1) +
matrix1 = np.matrix([[2,2,2], [2,2,2], [2,2,2]])
matrix2 = np.matrix([[3,3,3],[3,3,3],[3,3,3]])
print(matrix1)
print(matrix2)
r1 = matrix1 + matrix2
print(r1)

#2)-
r2 = matrix2 - matrix1
print(r2)

#3) *
r3 = matrix1 * matrix2
print(r3)

#4) /
r4 = matrix2 / matrix1
print(r4)

#5)**
r5 = matrix1 ** 2
r6 = matrix2 ** 2
print(r5)
print(r6)
#6)%
r7 = matrix2 % matrix1
print(r7)
#7) multiplication by scalar
r8 = matrix1 * 4
r9 = matrix2 * 3
print(r8)
print(r9)
#8) division by scalar
r10 = matrix1 / 2
r11 = matrix2 /1
print(r10)
print(r11)

"""Task 3.
Write a program that supports exception caused:
dividing by 0,
trying to open a non-existent file."""
try:
    f = 18/0
    print(f)
except ZeroDivisionError:
    print("It is not possible to divide anything to zero...")

try:
    f = open("no_such_a_file.txt")
except FileNotFoundError:
    print("File not found...")

"""Task 4.
Write a function that will report an exception while using it 
and handle it in the main part of the program."""

def func1():
    try:
        f = open("no_such_a_file.txt")
    except FileNotFoundError:
        print("File not found...")
    except:
        print("Something else went wrong:")
    else:
        print("Nothing went wrong:")
    finally:
        print("Function is finished")

func1()

