#!/usr/bin/env python3
import math

a= input(int())
b=input(int())
c= input(int())

#a= 1
#b=-1.5
#c= -1


print('solving ax^2 + c = 0:')
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))


d = ((b**2) - (4* a * c))

if d == 0:
    sol_2 = (-b+math.sqrt(b**2-4*a*c))/2*a
    print('roots: '+ sol_2)
elif d < 0:
    print('this equation has no solutions' )
else: 
    sol_1 = (-b-math.sqrt(b**2-4*a*c))/2*a
    sol_2 = (-b+math.sqrt(b**2-4*a*c))/2*a
    print('roots: ' + str(sol_1) + str(sol_2) )




