# Write a program to find the fictorial of a given number 

user_input = int(input("Enter the number: "))
product = 1
for i in range(1,user_input+1):
    product = product * i

print (f"Fictorial of the given number is {product}")
