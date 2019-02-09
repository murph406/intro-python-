#!/usr/bin/env python3

arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))


i = 0
x = 1


while i <= arrow_base_height:
    if i != 0:
        print('*' * arrow_base_width)
        i = i + 1
    else: 
        print()
        i = i + 1
while 0 != arrow_head_width: 
    print('*' * arrow_head_width)
    arrow_head_width = arrow_head_width - 1
