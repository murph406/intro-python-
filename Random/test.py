#!/usr/bin/env python3


def mostCommonK(dna, k):
    target = None
    count = 0
    maxCount = 0
    targetMaxCount = None
    for i in range(len(dna)-k+1):
        print(dna[i:i+k])
        target = dna[i:i+k]
        for j in range(len(dna)-k+1):
            print(target, dna[j:j+k])
            if target == dna[j:j+k]:
                count += 1
                if count > maxCount:
                    maxCount = count
                    targetMaxCount = target
        count = 0
    return targetMaxCount, maxCount

def runMostCommonSubstring(filename, minK, maxK):
    file = open(filename, 'r')
    dna = file.read()
    file.close()
    mostCommonSubstring(dna, minK, maxK)
    return mostCommonSubstring

def mostCommonSubstring(dna, minK, maxK)
    count2 = 0
    for i in range(minK, maxK):
        if maxCount > count2:
            count2 = maxCount
        return mostCommonK



