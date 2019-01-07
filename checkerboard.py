# Pratyusha Thundena
# October 5, 2017

from turtle import*

def drawaSquare(c):
    """To draw a checkerboard. The lower left corner should be at position 0,0
     and the board should be red and black, with each square being 20 pixels in size.
     The lower left corner should be black, and the pattern should be alternating
     black and red squares, for a total of 64 squares in an 8x8 pattern.
     """
    color(c)
    begin_fill()
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(20)
    end_fill()
    # increases the speed of the process of building a checkerboard
    speed(-100)

# starting from 0,0 position
goto (0,0)
# loop through 0-7
for x in range (8):
     for y in range (8):
         if (((x+y)%2 !=0)):
             drawaSquare('red')
         else:
             drawaSquare('black')
     penup()
     goto (0, (x+1) *20)
     pendown()
done()
# exits the program after user clicks it
exitonclick()


