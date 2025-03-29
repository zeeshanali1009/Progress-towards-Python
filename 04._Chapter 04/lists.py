# List is one of the important functionalities in python
# it is mutable means its values can be changed and its values are may be different
# it can have a single value for more then once means can have duplicate values 
this_list = [12,23,"Friends", 89.89,"Teachers", 7777]

print(this_list)

this_list.append("Zeeshan")   # this function will add the string at the end of the list 

this_list.insert(3,8888)       # this function will be adding the number 8888 at the index 3 

t_list  = [12,56,89,34,87,34,756]

t_list.sort()                   # this function will sort the list content in the ascending order
print(t_list)

t_list.reverse()                # this function will print the list in the reverse order 
print(t_list)

t_list.pop(3)                   # this function will pop out the value of the list using some specific index 
print(t_list)

print(t_list.pop(3))
print(t_list)

