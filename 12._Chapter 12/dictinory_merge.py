# In this program we will be discussing the merging process of the dictionaries 

first_dictionary = {"Zeeshan": 200, "Zohaib": 500}
second_dictionary = {"Zohaib": 500, "Zeeshan": 200, "Zain": 300}

merged_dictionary = first_dictionary | second_dictionary
print(merged_dictionary)
# merged dictionary will not print the same keys and values repeated in the both dictionaries