#!/usr/bin/env python3

f = open('happy.py', 'w')
for i in range(10):
    print('writing to the file:', i)
    f.write(str(i) + '/n')
f.close()



f = open('happy.txt', 'r')
for line in f:
    print('read from file', int(line))
f.close()
print('finished reading the file')

def read_nub_file ()