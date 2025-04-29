# dictionaries are the special functionalities of the python programming language which has 
# following functionalities
# mutable,unordered,indexed , cannot have duplicate values 
this_dictionary = {
    "Car" : "Ford",
    "Model" : "Mustang",
    "Year" : 2024,
     list :[12,78,90,90]
}

print(this_dictionary.items())


# Both of the functions given value have the same aim or same target but the differnces are :

print(this_dictionary.get("Expiry"))     #get function will print the none if value/key not found

print(this_dictionary["Expiry"])        #this will print the error if the key/value not found

