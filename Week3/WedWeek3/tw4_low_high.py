#!/usr/bin/env python3

lowInt = int(input('Low: '))
highInt = int(input('High: '))

if lowInt < highInt:
    while lowInt <= highInt:
        print(lowInt)
        lowInt += 1 
elif lowInt > highInt:
    while lowInt > highInt:
        print(highInt)
        highInt += 1 
else: 
    print('Something isnt right here????')
