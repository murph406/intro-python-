#!/usr/bin/env python3

triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

i = 0
j = 0

for i in range(triangle_height + 1):
    for j in range(i):
        print(triangle_char, end = ' ')

    print('')
        
    
