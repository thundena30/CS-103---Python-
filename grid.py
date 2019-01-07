#Pratyusha Thundena
#September 18,2017

def grid():
    """ To draw 10 black vertical and 10 black horizontal
     lines in grid form
     """

import turtle                       # Allows us to use turtle library
sunny = turtle.Turtle()
sunny.pensize(3)                    # Determines pen thickness

def square(side):
    for i in range(4):
        sunny.forward(side)
        sunny.left(90)
        sunny.speed(0)
def row(n, side):
    for i in range(n):
        square(side)
        sunny.forward(side)
    sunny.penup()
    sunny.left(180)
    sunny.forward(n * side)
    sunny.left(180)
    sunny.pendown()
    sunny.speed()
def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side)
        sunny.penup()
        sunny.left(90)
        sunny.forward(side)
        sunny.right(90)
        sunny.pendown()
    sunny.penup()
    sunny.right(90)
    sunny.forward(m * side)
    sunny.left(90)
    sunny.pendown()
    sunny.speed()

row_of_rows(10,10, 20)                 # Creates 10 x 10 square grid
turtle.exitonclick()                   # Exits the turtle program with a click

