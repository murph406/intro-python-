#!/usr/bin/env python3

# python sandpiles.py

def printPile(data):
    for x in data: 
        print(x)
    
    row1 = data[0]
    row2 = data[1]
    row3 = data[2]
    
    print("row1 =", row1, "row2 =", row2, "row3 =", row3)
    
    isStablePile(data, row1, row2, row3)

def isStablePile(pile, row1, row2, row3):
    total = 0
    for q in pile:
        if q[0] > 3:
            total += 1
            
    
    for w in pile:
        if w[1] > 3:
            total += 1

    for r in pile:
        if r[2] > 3:
            total += 1

    topplePile(pile, total, row1, row2, row3)

def topplePile(pile, total, row1, row2, row3):
    if total == 0:
        print('Pile is Stable')
    else: 
        print('Pile is not Stable')
        for x in row1:  
            if x > 3:
                print(row1.index(x))
                
               


printPile([(2,4,4),(2,3,0),(2,0,2)])