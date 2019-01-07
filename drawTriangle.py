#Pratyusha Thundena
#September 28,2017

# imports Turtle library
from turtle import *

def drawTriangle(x,y):
    """ To draw a filled blue triangle using forward() and left() functions"""

    # create a turtle object
    franklin = Turtle()


    franklin.pensize(4)
    franklin.fillcolor("blue")
    franklin.begin_fill()
    # pepup to move the turtle without drawing
    franklin.penup()
    # move the turtle to a given location
    franklin.goto(x, y)
    # pendown to move the turtle with drawing
    franklin.pendown()
    # using forward and left to draw a triangle from given x and y.
    for i in [0, 1, 2]:
        franklin.forward(175)
        franklin.left(120)
    franklin.end_fill()

# call the function
drawTriangle(-50, -50)
exitonclick()

