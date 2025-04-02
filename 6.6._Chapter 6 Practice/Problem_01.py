# Write a program to print the greatest number from given 4 numbers 
a1= int(input("Enter the number: "))
a2= int(input("Enter the number: "))
a3= int(input("Enter the number: "))
a4= int(input("Enter the number: "))

if (a1>a2 and a1>a3 and a1>a4):
    print("First  number is greatest of all the given numbers : a1")

if (a2>a1 and a2>a3 and a2>a4):
    print("Second  number is greatest of all the given numbers : a2")

if (a3>a1 and a3>a2 and a3>a4):
    print("Third  number is greatest of all the given numbers : a3")

if (a4>a1 and a4>a2 and a4>a3):
    print("Fourth  number is greatest of all the given numbers : a4")