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

# Draw the Level 3 version of the room
window = room.draw_room(level = 3,radius=5)

###
# Start your code here
step=40
r=5
forward(step)
right(90)
for i in range(4):
    forward((r-2)*step)
    left(90)
    forward(step)
    right(90)
    forward(step)
    left(90)
    forward((r-2)*step)
    right(90)
    forward(step)
    backward(step)
    left(90)    
for i in range(3):
    left(90)
    forward(step)
    right(90)
    for j in range(4):
        forward(step*(3-i))
        left(90)
        forward((3-i)*step)
left(90)
forward(step)
 
# End your code here
###
 
window.exitonclick()