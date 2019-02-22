#!/usr/bin/env python3

x = int(input("pick an integer for x"))
y = int(input("pick an integer for y"))
z = int(input("pick an integer for z"))

list = [x, y, z]

answer_1  = int(input("would you like to find the highest odd or even?"))

if answer_1 == 'odd':
    if x % 2 == 1:
        print('x is odd')
    else:
        list.remove(x)
    if y % 2 == 1: 
        print('y is odd')
     else: 
        list.remove(y)
     if z % 2 == 1: 
        print('z is odd')
    else: 
        list.remove(z)
else answer_1 == 'even':
    if x % 2 == 0:
        print('x is even')
    else:
        list.remove(x)
    if y % 2 == 0: 
        print('y is even')
    else: 
        list.remove(y)
    if z % 2 == 0: 
        print('z is even')
     else: 
        list.remove(z)
    print('The maximum', answer_1, 'number is',max(list),'.')



