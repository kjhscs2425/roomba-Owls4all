# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1,radius=5)

###
# Start your code here
speed(10)
def step(boxes=1):
    forward(40*boxes)
def back(boxes=1):
    backward(40*boxes)
r=5
step(2*r)
back()

for i in range(3):
    right(90)
    step()
    left(90)
    back(2*(r-1))
    step(2*(r-1))
back()
right(90)
step()
left(90)
back(6)
step(3)
right(90)
step()
back(14)
step(2)
left(90)
step(2)
back(4)
step(1)
right(90)
for i in range(2):
    step()
    left(90)
    step(2)
    left(90)
    step()
left(90)
step()
right(90)
step(3)
for i in range(4):
    if i ==0:
        r=3
    else:
        r=4
    right(90)
    step(r)
    back(2*r)
    step(r)
    left(90)
    step()

 
 
# End your code here
###
 
window.exitonclick()