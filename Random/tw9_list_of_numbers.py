#!/usr/bin/env python3


def inputList3():
    list = ''

    print("Enter a series of integers divisible by 3: ")
    x = input()
   
    while x != "STOP":
        y = x / 3.0
        if (y).is_integer():å
            list += str(x)
            print(list, "yup")
            print("Next: ")
            x = input()
        else:
            print(list, "nope")
            print("Next: ")
            x = input()
    print(list)

inputList3()