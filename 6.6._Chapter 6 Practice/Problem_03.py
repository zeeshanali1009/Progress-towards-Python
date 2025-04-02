# Write a program to detect the spam messages 
# "Make a lot of money"  , "buy now" , "subscribe this"  , "Click this"

user_input = input("Enter the input")

if user_input == "Make a lot of money" or user_input == "Buy now" or user_input== "Subscribe this" or user_input == "Click this":
    print("Given data is spam")
else:
    print("Given data is not spam! All good.")
    