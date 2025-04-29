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
    a = print(f"Hello {name}")
    return "done"

# this will definetely return something "done" at the function calling 
a = greet("Zeeshan", "Good Bye!")
print(a)
# this will give none in the output because in the function definition we have not retuned any thing 
greet("Zeeshan")
