# Write a program to print the multiplication table of a number 
# Write a program to print the table in the reverse order

user_input = int(input("Enter the number: "))
for i in range (1,11):
    print(f"{user_input} X {11-i} = {(user_input)*(11-i)}")