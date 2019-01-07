#Pratyusha Thundena
#September 18,2017

def light_green_sqr():
    """ To create a new shape (light green rectilinear square)
     and to use the goto() function for direction
     """


from turtle import *            # Another way of importing the turtle library

pensize(4)                      # Increases the thickness of the pen
color('light green')
goto(100,0)                     # goto() is another way to move direction
right(90)
goto(100, -100)
left(90)
goto(0, -100)
left(90)
goto(0,0)
right(90)


exitonclick()




