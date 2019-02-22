#!/usr/bin/env python3

def deepSum(x):
    numberSet = []
    i = 0

    data = str(x)
    data2 = data.replace(" ","")
    data3 = data2.replace("(","")
    data4 = data3.replace(")","")
    data5 = data4.replace(",","")

    while i < len(data5):
        numberSet.append(int(data5[i]))
        i += 1
    print(numberSet)
    print(sum(numberSet))

deepSum(((1, 2, 3), (4, 5, 6), (6,), (), (7, 8, 9)))
