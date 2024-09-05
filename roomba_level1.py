# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Athena
# -----------------------------------------------------------------------------
 
from turtle import left, forward, backward
import room

# Draw the Level 1 version of the room
window = room.draw_room(level = 1)

###
# Start your code here
SquareSize=40
YSquares=5
Xsquares=5
def go(stepsize,xsteps,ysteps,startx,starty):
    if(starty=='top'): 
        for i in range(xsteps):
            forward(stepsize*ysteps)
            if i%2==0:
                left(90)
            else:
                left(270)
            forward(stepsize)
            if i%2==0:
                left(90)
            else:
                left(270)
    else:
        for i in range(xsteps):
            forward(stepsize*ysteps)
            if i%2==1:
                left(90)
            else:
                left(270)
            forward(stepsize)
            if i%2==1:
                left(90)
            else:
                left(270)
    forward(stepsize*ysteps)
go(40,Xsquares-1,YSquares-1,'left','top')
 
# End your code here
###
 
window.exitonclick()