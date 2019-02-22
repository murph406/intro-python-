#!/usr/bin/env python3
x = ["ryan", "john", "pat"]

def append(seq, suffix):
    """Tack on the siffox to the end of every string in seq"""
    for elem in seq:
        elem += suffix
        print(elem)

append(x, ' is the Best!!!!!')