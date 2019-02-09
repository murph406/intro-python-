#!/usr/bin/env python3
a= 1
b= -1.5
c= -1

epsilion = 0.001
guess = 1.0
i = 0

print('solving ax^2 + c = 0:')
print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('initial guess: ' + str(guess))

def f(x):
    return x**a + b*x - c

def fPrime(x):
    return a*x + b

while abs(f(guess)) >= epsilion:
    guess = guess - (f(guess)/fPrime(guess))
    i += 1

print('one root is: ' + str(round(guess,3)))
print('took ' + str(i) + ' iterations')

