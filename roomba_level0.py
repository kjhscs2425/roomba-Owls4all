# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Athena
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
SquareSize=40
YSquares=5
Xsquares=5
turtleX=1
turtleY=5
def go(stepsize,xsteps,ysteps):
    forward(stepsize*ysteps)
    left(90)
    for i in range(4):
        forward(stepsize*(xsteps-i))
        left(90)
        forward(stepsize*(ysteps-i))
        left(90)
go(40,Xsquares-1,YSquares-1)


# End your code here
###
 
window.exitonclick()