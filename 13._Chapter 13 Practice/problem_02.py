# create a program take the input from the user and then format is using the format function as well

name = input("Enter your name : ")
Phone_no = input("Enter your Phone no : ")
Address = input("Enter your Address : ")

result = "{} 's phone number is {} and he is living in {}".format(name,Phone_no,Address)
print(result)