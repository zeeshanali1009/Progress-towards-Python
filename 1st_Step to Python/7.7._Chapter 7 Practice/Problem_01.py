# Write a program to print the multiplication table of a number 

user_input = int(input("Enter the number: "))
for i in range (1,11):
    print(f"{user_input} X {i} = {user_input*i}")