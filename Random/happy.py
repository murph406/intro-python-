#!/usr/bin/env python3

original_list = ['123' , '123', '124', '125', '123' ]

def removeDuplicates(listofElements):  
    # Create an empty list to store unique elements
    uniqueList = []  
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList
 
def main():  
    '''
        Removing duplicates from a List by keeping the Order
    '''
    # List of Numbers with duplicates
    listOfNums = [10, 2, 45, 3, 5, 7, 2 , 10, 45,  8, 10]
    print("Original List : " , listOfNums)
            
    listOfNums = removeDuplicates(listOfNums)
    
    # Now list contains unique elements only
    print("List with unique elements : ", listOfNums)
      
main()