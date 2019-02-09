#!/usr/bin/env python3

import random

print('I am aguessing game choose a number between 1 and 100')

secret = random.randint(1,100)

guess = int(input('Guess that number! '))

while guess!= secret:
    if guess < secret < 100:
        print('too low')
    elif guess < 100:
        print('Guess Lower')
    else:
        print('too high!')
    guess = int(input('Try Again! '))
print('you got it!')

