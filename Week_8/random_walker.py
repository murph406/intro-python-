#!/usr/bin/env python3

import turtle
import random 
import math

x = 0
def get_rand_int():
    return random.randint(0, 360) 
class Escape(object):
   
    def __init__(self, dist, rad):
        self.dist = dist
        self.rad = rad

    def fence(self):
        bob = turtle.Turtle()
        bob.circle(self.rad) 
    
    def align(self):
        jim = turtle.Turtle()
        jim.penup()
        jim.penup()
        jim.left(90)
        jim.forward(self.rad)
    
    def capture(self):
        jim = turtle.Turtle()
        '''sara.right(random.randint(0, 360))'''
        jim.forward(self.dist)
          
    def stop(self):
        input()

x = Escape(20, 100)
x.fence()
x.align()
x.capture()
x.stop()


''''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()'''''

'''
class Escape(object):

    def __init__(self, r = 200, forward = 30):
        self.r = float(r)
    
    def fence(self):
        turtle.penup()
        turtle.setpose(0, -(self.r))
        turtle.pendown
        turtle.circle(self.r)
        turtle.penup
        turtle.home()
        turtle.pendown()
    
    def escape(self):
        while turtle.distance(0,0) < self.r:
            movement =random.randint(0,200)
            degree = random.randint (0,360)
            turtle.right(degree)
            turtle.forward(movement)
    def capture(self):
        turtle.penup()
        turtle.home()
        turtle.pendown()
'''


