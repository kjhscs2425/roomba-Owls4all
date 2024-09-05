# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Athena
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
SquareSize=40
YSquares=15
Xsquares=20
def go(stepsize,xsteps,ysteps,startx,starty):
    if(starty=='top'): 
        for i in range(xsteps):
            forward(stepsize*ysteps)
            if i%2==0:
                left(90)
            else:
                right(90)
            forward(stepsize)
            if i%2==0:
                left(90)
            else:
                right(90)
    else:
        for i in range(xsteps):
            forward(stepsize*ysteps)
            if i%2==1:
                left(90)
            else:
                right(90)
            forward(stepsize)
            if i%2==1:
                left(90)
            else:
                right(90)
    forward(stepsize*ysteps)

go(40,Xsquares-1,YSquares-1,'left','top')
 
# End your code here
###
 
window.exitonclick()