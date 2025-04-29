# Write a program to find whether the given user input contains the length of characters is less then 10

user_input = input("Enter the word: ")

if len(user_input) > 10:
    print("Limit exceeded! Chracters are more then 10.")
else:
    print("Everything is in-check and character length is not exceeded!")