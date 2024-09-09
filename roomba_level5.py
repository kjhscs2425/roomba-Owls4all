# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Athena
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# THIS PARAMETER CAN CHANGE!!!
# Make sure your code works for n_alcoves = 0, 1, 2, 3, and 4
# (You are allowed to use this parameter in your code)
n_alcoves = 4

# Draw the Level 5 version of the room
window = room.draw_room(level = 5, n_alcoves = n_alcoves,radius=5)

###
# Start your code here
speed(10)
def step(boxes=1):
    forward(40*boxes)
def back(boxes=1):
    backward(40*boxes)
def alcove(exitAngle):
    step(4)
    back(2)
    left(90)
    step(2)
    back(4)
    step()
    left(90)
    step()
    for i in range(3):
        right(90)
        step(2)
    back()
    left(90)
    back()
    left(exitAngle)
    step(3)
def checkAlcove(corner): #alcove order 3, 1, 0, 2
    if corner ==0:
        if n_alcoves >= 3:
            return True
        else:
            return False
    if corner ==1:
        if n_alcoves >= 2:
            return True
        else:
            return False
    if corner ==2:
        if n_alcoves >= 4:
            return True
        else:
            return False
    if corner ==3:
        if n_alcoves >= 1:
            return True
        else:
            return False    
def corner(corner):
    right(90)
    step(3)
    left(90)
    step()
    right(90)
    step()
    left(90)
    step(3)
    right(90)
    step()
    if checkAlcove(corner):
        alcove(180)
    else:
        left(180)
        step()
if n_alcoves >=3:
    step(5)
else:
    step()
corner(1)
corner(2)
corner(3)
corner(0)
step()
left(90)
for i in range(3): 
    step(3-i) 
    right(90)
    for j in range(3):
        step(2*(3-i))
        right(90)
    step(3-i)
    right(90)
    step()
    left(90)

 
# End your code here
###
 
window.exitonclick()