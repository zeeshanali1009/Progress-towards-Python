# Write a program to print the 3rd,5tdh and 7th item of the list 
this_list = [1,2,3,4,5,6,7,8]

for index,item in enumerate(this_list):
    if (index==3 or index ==5 or index ==7 ):
        print(item)