#!/usr/bin/env python3

mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

for x in mult_table: 
    for y in x:
        
        print(y, end=" | ")
    print()