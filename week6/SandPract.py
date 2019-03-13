#!/usr/bin/env python3

# python SandPract.py

a = [[2,0,2],[0,3,0],[2,0,2]]

def isPrint(a):
    for x in a: 
        print(x)
    isStable(a)
   

def isStable(a):
   
    for row in a:
        for cell in row:
            if 0 <= cell <= 3:
                print(row, "True")
                return True
    print(row, "False")
    return False
    
isPrint([[2,0,2],[0,3,0],[2,0,2]])

