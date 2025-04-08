# We can raise the exceptions as well as sometimes the fault is critical so we haveto raise the exceptions
# as well

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if (b==0):
    raise ZeroDivisionError("Our program is not meant to divide a number by 0")
else:
    print(f"The division of the given numbers is {a/b}")