# dictionaries are the special functionalities of the python programming language which has 
# following functionalities
# mutable,unordered,indexed , cannot have duplicate values 
# Actually dictionary are designed to make the look up process easy 
this_dictionary = {
    "Car" : "Ford",
    "Model" : "Mustang",
    "Year" : 2024
}

# prints the content present in the dictionary 
print(this_dictionary)

# prints all the value on the output
print(this_dictionary.items())

# Prints the keys present in the dictionary 
print(this_dictionary.keys())

# prints the values of the keys present in the dictionary
print(this_dictionary.values())

# updates the different values present in the dictionary 
print(this_dictionary.update({"Car": "BMW","Model":"Classis", "Manfuctured": "2020"}))
print(this_dictionary)
