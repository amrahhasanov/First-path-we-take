"""Task 3*.
Write a program to draw the fractal shown on the next page."""
from turtle import *
window = Screen()
speed(100)
right(30)
shape("triangle")
hideturtle()

def sierpinski(length, depth):
    if depth == 0 :
        pd()
        stamp()
        pu()
    else:
        pu()
        for i in range(0,3):
            forward(length)
            sierpinski(length/2,depth -1)
            backward(length)
            left(120)
sierpinski(200,5)
window.exitonclick()
