''' Sandpiles

Author: Kevin Lundeen
For: CPSC 1220, HW 5
'''
def printPile(a):
    ''' Prints out a sandpile nicely.
        >>> printPile([[2,0,2],[0,3,0],[2,0,2]])
        [2, 0, 2]
        [0, 3, 0]
        [2, 0, 2]
        
    '''
    for row in a:
        print(row)
    print()

def isStablePile(a):
    ''' Is given sandpile stable, i.e., have values all between 0 and 3?
        >>> isStablePile([[0,1,2],[2,3,2],[0,0,1]])
        True
        >>> isStablePile([[0,4,0],[3,5,3],[1,2,3]])
        False
    '''
    for row in a:
        for cell in row:
            if not 0 <= cell <= 3:
                return False
    return True

def topplePile(a):
    ''' Topple any cells that have 4 or more by moving 4 pieces to surrounding
        cells.

        >>> topplePile([[0,0,0],[0,4,0],[0,0,0]])
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        >>> topplePile([[4,0,0],[0,4,0],[0,0,0]])
        [[0, 2, 0], [2, 0, 1], [0, 1, 0]]
        >>> topplePile([[4,0,0],[0,10,0],[0,0,0]])
        [[0, 3, 0], [3, 2, 2], [0, 2, 0]]
    '''
    while not isStablePile(a):
        for row in range(len(a)):
            for col in range(len(a[row])):
                if a[row][col] > 3:
                    a[row][col] -= 4
                    if row > 0:
                        a[row - 1][col] += 1
                    if row + 1 < len(a):
                        a[row + 1][col] += 1
                    if col > 0:
                        a[row][col - 1] += 1
                    if col + 1 < len(a[row]):
                        a[row][col + 1] += 1
    return a

def addPiles(a, b):
    ''' Add two 3x3 sandpiles (a list of 3 lists each of integers
        from 0 to 3) toppling the result until it is stable.
        See: https://en.wikipedia.org/wiki/Abelian_sandpile_model.

        >>> addPiles([[0,0,0],[0,2,0],[0,0,0]], [[0,0,0],[0,2,0],[0,0,0]])
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        >>> addPiles([[1,2,0],[2,1,1],[0,1,3]], [[2,1,3],[1,0,1],[0,1,0]])
        [[3, 3, 3], [3, 1, 2], [0, 2, 3]]
    '''
    result = []
    for row in range(len(a)):
        result.append([])
        for col in range(len(a[row])):
            result[row].append(a[row][col] + b[row][col])
    return topplePile(result)

def zeroPile():
    ''' This is the sandpile that when added to any sandpile in the 3-generated
        group returns the same sandpile.
        
        >>> zeroPile()
        [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
        >>> addPiles([[3,3,3],[3,3,3],[3,3,3]], zeroPile())
        [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    '''
    return [[2,1,2],[1,0,1],[2,1,2]]

def isInGroup(a):
    ''' Check if sandpile a is in the 3-generated group.
        >>> isInGroup([[3,2,2],[2,1,1],[3,3,3]])
        True
        >>> isInGroup([[1,1,1],[1,1,1],[1,1,1]])
        False
    '''
    return addPiles(a, zeroPile()) == a

def countGroup():
    ''' Count all the 3x3 sandpiles that are in the abelian group (those
        that satisfy isInGroup). Also print out every 10,000th sand pile
        along the way. '''
    inGroup = 0
    count = 0
    for i1 in range(4):
        for i2 in range(4):
            for i3 in range(4):
                for i4 in range(4):
                    for i5 in range(4):
                        for i6 in range(4):
                            for i7 in range(4):
                                for i8 in range(4):
                                    for i9 in range(4):
                                        pile = [[i1,i2,i3],[i4,i5,i6],[i7,i8,i9]]
                                        if isInGroup(pile):
                                            inGroup += 1
                                        count += 1
                                        if count % 10000 == 0:
                                            printPile(pile)
                                            if isInGroup(pile):
                                                print('is in group')
                                            else:
                                                print('is not in group')
                                            print()
    return inGroup, count
