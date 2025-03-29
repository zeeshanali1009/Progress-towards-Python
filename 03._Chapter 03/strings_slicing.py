# We will be discussing the strings in the details
# First of all the strings are the mutable ones like they cannot be changed
# let suppose there is a string [Zeeshan] have both the positive index values as well the negative index 
# values too  like [0,1,2,3,4,5...] starts from the left to right
# and the negative index values too  [,.....-5,-4,-3,-2,-1] starting from right to left 
name = "Zeeshan"
print(name)

print(name[0:3])     #it will print Zee  (3 represents l-1)  and printed indexes are 0,1,2

print(name[:4])       # It will print Zees (empty space before colon represent 0 and 4 represents l-1) 
                        # printed indexes are the 0,1,2,3

print (name[0:])    # It will print Zeeshan (empty space after colon represent l and 0 is starting index) 
                        # printed indexes are the 0,1,2,3,4,5,6


# This process is called string slicing means slicing the indexes and there are two types which are
# Positive Index Slicing  (using the positive index values starting from the 0 from left to right)
# Negative Index Slicing  (using the negative index values starting from the -1 from right to left)
# Skip value slicing 

print(name[0:6:3])     # 0 represents the starting index 6 represents the ending index for the search 
                        # purpose and 3 represents the skipping jump value 






