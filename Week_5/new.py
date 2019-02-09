#!/usr/bin/env python3

# Emma Gloekler gloekler@seattle


def inputToFile(fileName):
 
    f = open(fileName, 'w')
    i = ''
    while i != 'DONE': 
       i = input(str('write something'))
       f.write(str(i) + '/n')
    f.close()
    print('finished')

inputToFile('teest.py')
