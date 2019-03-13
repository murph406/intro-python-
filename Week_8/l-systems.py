#!/usr/bin/env python3

import turtle

def drawPile(size, color):
    ''' Draw a 3x3 sandpile on the screen with blue for cells with 0, yellow
    for cells with 1, orange for 2, red for 3. Size determines size of
    individual cells in the drawing. '''
    colorMap = {0:'blue', 1:'yellow', 2:'orange', 3:'red'}
    bob = turtle.Turtle()
    bob.color('black', colorMap[color] )

    bob.begin_fill()
    bob.forward(size)  # draw top
    bob.right(90)
    bob.forward(size)  # draw right side
    bob.right(90)
    bob.forward(size)  # draw bottom
    bob.right(90)
    bob.forward(size)  # draw left side
    bob.end_fill()
    input()
  
def rewrite(values, rules, n):
 ''' Word is a string that is a sequence of letters from the alphabet of an
 L-system. Productions is a dictionary of replacement rules--the keys are
 letters in the L-system alphabet and the values are the replacement
 string for the given key. N is the number of times to transform
 the word through the productions.

rewrite('A', {'A':'AB','B':'A'}, 4)
'ABAABABA'
'''
     for x in range(n):
         newValue = ''
          for character in values:
              if character in rules:
                newValue += rules[character]
            else:
                newValue += character       
    return newValue

def render(word, angle=25, forward=8, position=(0, -300), heading=90):
 ''' Word is a string which is a derivation of an L-system (results from
 rewrite). Executes each letter in word as a rendering command.
 'F' means go forward (using the forward parameter for how far).
 'R' same as 'F' (since some systems need another F).
 'X' is ignored (just used to control how the rewrite progresses).
 '-' means rotate right angle degrees.
 '+' means rotate left angle degrees.
 '[' means push current drawing state onto stack (to be popped by
     corresponding ']' latter in word)
 ']' means pop previously pushed state from matching previous '[' in word
 '''
    for cmd in word:
          if cmd == 'F':
            aTurtle.forward(forward)
        elif cmd == 'R':
            aTurtle.forward(forward)
        elif cmd == '-':
            aTurtle.right(angle)
         elif cmd == '+':
            aTurtle.left(angle)
        elif cmd == '[':
            position, heading = stack.pop()
         elif cmd == ']':
              stack.append((turtle.position(), turtle.heading()))
        else:  
            print('Error:', cmd, 'is unknown ')
