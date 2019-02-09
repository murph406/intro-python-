#!/usr/bin/env python3

import random 

list1=[]

for ran_int in range(10000+1):
    list1.append(random.randint(-10000, 10000))

odd_list= [odd for odd in list1 if odd % 2 == 1]
even_list=[even for even in list1 if even % 2 ==0]
ratio =  len(odd_list) / len(even_list)
list_0 = [len(str(list1==0))]
list_1000 = [len(str(list1 == 1000))]
list_10002 = [len(str(list1 == -1000))]


print('number of 0', list_0, 'Number of 1000', list_1000,'number of -1000',list_10002 )
print('the ratio is', ratio,'even to odd numbers')
print('All the odd numbers are', odd_list)
print('All the even numbers are', even_list)
