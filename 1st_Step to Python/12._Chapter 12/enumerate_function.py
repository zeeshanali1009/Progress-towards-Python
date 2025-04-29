# enumerate function add the counter to the iterable and then returns it 

this_list = [12,34,56,34,34,32]
# index =0
# for item in this_list:
#     print(f"the value at the index {index} is {item}")

# now this same process can also be carried out using the enumerate function as well

for index,item in enumerate(this_list):
    print(f"the value at the index {index} is {item}")
