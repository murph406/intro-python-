#!/usr/bin/env python3

'''patterns we know so far'''

import random

'''def makeTuple(count, low, high):
    Make a tutple of lenghth, count, with random numbers, 
    with random int between lo high and inclusive and return the tupil
    ret = ()

    for i in range(count):
        ret += (random.randint(low, high), )

    print(ret)

makeTuple(10, 0, 100)

def makeList(count, low, high):
    ret = []

    for i in range(count):
        num = random.random()

        ret.append(num)

    print(ret)

makeList(10, 0, 100)'''

def getLineLegth(file):
    '''Open Text File and read through the lines and return the average line length'''
     
    file = open(file, 'r') 
    num_lines = 0 
     
    for lines in file:
        num_lines += 1

    file.close()
    print(num_lines) 
    
'''getLineLegth(input("enter file"))'''

'''
New Data Types
    list - [] [16] [1,2, 'hello']
    dict - {} d[1,2,3] => returns values
    tuple - () (32,) (1,2,3)
    file - file.close, file.open
    def - return 
how to assign a variable 
    assignment: = += -=
    for loop: 
    paramenters filed in by callers argument 
    def ___ assigns a funciton object to that variable 
    __________
    aliassing
    mutable objects and dictionary 
        useing indecing or methods like append 
        x[3]=120
        d[(1,2)] or d['key']'''


list = {
    "Name": "Jim",
    "Age": 27,
    "Date": 1991,
}


def isReversed(list):
    newList = {}

    for x in list:
        newList[list[x]] = x
   
    print(newList)

isTrueFalse(list)