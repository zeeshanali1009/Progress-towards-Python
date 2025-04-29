# list comprehension is one of the important method to create the lists using the already existing lists
# in the below program the other list has been created using the existing list
this_list = [56,89,9,56,98]

another_list =[]

another_list = [i*i for i in this_list]

print(another_list)



# for item in this_list:
#     another_list.append(item*item)
# can be replaced using the only one line as 
# another_list = [i*i for i in this_list]