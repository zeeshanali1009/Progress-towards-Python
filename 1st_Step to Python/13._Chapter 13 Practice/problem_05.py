
 # Write a program to find the maximum number from the list using the reduce function

from functools import reduce

this_list =[12,34,56,68,34,68,89,34,68,89]

def greater_number(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater_number,this_list)) 
