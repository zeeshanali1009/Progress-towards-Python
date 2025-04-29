# for loop is used when we know the range
# for loop can also be used to print the content of list, tuple (iteratable)

for i in range(1,6):
    print(i)

# for loop use in the printing of list content
this_list = [12,23,45,567,78,89]
for i in this_list:
    print(i)

# for loop use in the printing of tuple content
this_list = (12,23,45,567,78,89)
for i in this_list:
    print(i)

# loops are also used with the else statements like when the lopp is exhausted the else statement gets executed 
this_list = (12,23,45,567,78,89)
for i in this_list:
    print(i)
else:
    print("done")

# range function with the slicing
# range(starting, ending, jump)
for i in range(1,100,6):
    print(i)
