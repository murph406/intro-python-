#!/usr/bin/env python3

def wordByPrefix(prefSize, list):
    ret ={}
    for word in list: 
        prefix = word[:prefSize]
        if prefix not in ret:
            ret[prefix] = [word]
        else: 
            ret[prefix].append(word)
        
    return print(ret)


def xxxwordByPrefix(prefSize, list):
    ret = []
    for word in list: 
       ret.append(word[:prefSize]) 
    return print(ret)

wordByPrefix(2, ['able', 'ability', 'apple', 'tryst', 'trial', 'tremendous', 'tree'])
{'tr': ['tryst', 'trial', 'tremendous', 'tree'], 'ab': ['able', 'ability'], 'ap': ['apple']}

