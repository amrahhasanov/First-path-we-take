"""Task 1.
Write a program containing instructions for drawing an equilateral triangle ."""
import  turtle
window = turtle.Screen()
"""turtle.bgcolor("red")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.pendown()"""

for i in range(3):
    turtle.forward(300)
    turtle.left(120)
"""turtle.end_fill()"""
window.exitonclick()


