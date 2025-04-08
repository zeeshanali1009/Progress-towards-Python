# Write a program to check the use of zero division error 
try: 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a/b)
except Exception as e:
    print("Infinite")