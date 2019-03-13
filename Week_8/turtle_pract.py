#!/usr/bin/env python3

import numpy as np
from turtle import *
import random 
import math


# setting up screen
reset()
screensize(550)
Screen().bgcolor('black')
tracer(0)

# drawing box
t0 = Turtle()
t0.penup()
t0.goto(-256,-256)
t0.color('cyan')
t0.pendown()
for i in range(4):
    t0.forward(512)
    t0.left(90)
t0.ht()

# parameters
velocity = 5
iterations = 200
boxsize = 512
ranheader = np.random.random()*360
ranx = np.random.random()*boxsize
rany = np.random.random()*boxsize

class turtle_agents(Turtle):
    def _init_(self):
        self.up()
        self.seth(ranheader)
        self.setpos(ranx,rany)
        self.velocity = velocity
        self.down()

# turtle
t1 = turtle_agents()
t1.color('green')
t2 = turtle_agents()
t2.color('blue')

# turtle movement
for turtle in turtles():
    for i in range(iterations):
        turtle.forward(velocity)
        if turtle.xcor() >= 256:
            turtle.goto(-256,t0.ycor())
        elif turtle.xcor() <= -256:
            turtle.goto(256,t0.ycor())
        elif turtle.ycor() >= 256:
            turtle.goto(t0.xcor(),-256)
        elif turtle.ycor() <= -256:
            turtle.goto(t0.xcor(),256)

update()    
exitonclick()