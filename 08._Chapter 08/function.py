# functions are the most important functionality of the programming to make the set of instruction in use 
# by simply calling the function


def average():
    a= int(input("Enter the number: "))
    b= int(input("Enter the number: "))
    c= int(input("Enter the number: "))
    average = (a+b+c) / 3
    print(f"Average of the given numbers is {average}")

average()

# by passing arguments
# there can be multiple arguments

def greet(name):
    print(f"Hello {name}")

greet("Zeeshan")

# by default arguments

def greet(name, endline = "Thank You!"):
    print(f"Hello {name}")
    print(endline)

greet("Zeeshan")
greet("Zeeshan", "Good Bye!")
