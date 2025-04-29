# sets have the following properties 
# unordered , cannot have duplicate values 

this_set = {12,34,56,78,"Zeeshan"}

# printing the length of the set
print(this_set.len())

# for removing specific item from the set 
print(this_set.remove(12))

# for removing or deleting the random item form the set 
print(this_set.pop())

# for clearing the all set 
print(this_set.clear())



set_1 ={34,56,78,23,23,7}
set_2 = {12,76,34,78,32,132,7}

# printing the union od two sets
print(set_1.union(set_2))

# printing the intersection od two sets
print(set_1.intersection(set_2))