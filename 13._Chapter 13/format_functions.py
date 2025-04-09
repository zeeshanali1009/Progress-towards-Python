# format function has also been in use for formatting the string actually it has been used in the place of 
# fstring before the use of fstrings but it is now used very much rarely but we need to know about it

result = "{} is a good {}".format("Zeeshan", "student")
print(result)

# we can also change the position of different list elements using the index as 
result = "{1} is a good {0}".format("Zeeshan", "student")
print(result)