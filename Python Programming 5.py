#Python 5
"""Task 1.
Import the math package, use its functions to calculate the values of the following mathematical expressions
(x is a variable previously entered by the user):
"""
#1.1
import math
x = float(input("x: "))
w1 = 4 * math.sqrt(x + 6)
print(w1)

#1.2
w2 = 3 * (x**3)+ 4 * (x**2) - 5 * x +math.sqrt(7)
print(w2)

#1.3
w3 = 1 / math.sqrt(2 * (x**2) + 3 * x - 9)
print(w3)

#1.4
w4 = abs(2 * x)
print(w4)
#1.5

w5 = 1 / math.e ** x
print(w5)

#1.6

w6 = 6 * math.sin(x) - 5

"""Task 2.
Write a program displaying in the form of a table the results of any function using  sinus, cosinus.
"""
import math
T = float(input("Enter the number:"))
sin = math.sin(T)
print("sin at", T, "is equal to: ", sin)
cos = math.cos(T)
print("cos at", T,"is equal to: ",cos)

"""Task 3.
Modify the program from Task 2 so that the function is displayed as a graph. 
Use the functions from the matplotlib.pyplot module for this."""

"""Task 4.
Add to the graph received in task 3:
⦁	the title of the chart,
⦁	axle descriptions,"""

"""Task 5.
Complete the program from Job 3 so that the image is automatically saved to file."""
