# Write a program to verify that whether the given input is present or not 

user_input = input("Enter the input: ")

# if ("Zeeshan" in user_input):
#     print("Zeeshan is Present!")
# else:
#     print("Zeeshan is not present!")

# Upper condition is case sensitive 
# Difference among them is as
#Lower condition is not case sensitive like camparison is made after making them in lower case 

if ("Zeeshan".lower() in user_input.lower()):
    print("Zeeshan is Present!")
else:
    print("Zeeshan is not present!")