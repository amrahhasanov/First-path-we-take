"""Task 2.
Write a program that allows you to draw the fractal shown below:"""
import turtle
window = turtle.Screen()
turtle.speed(100)
a = 1
for i in range(28):
    a += 2*a/10
    for i in range(4):
        turtle.forward(a)
        turtle.right(270)

window.exitonclick()