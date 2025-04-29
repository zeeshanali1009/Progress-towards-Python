# Write a program to create a dictionary with the english words alongwith their translations and then 
# print them according to the user input

infrormation_dictionary = {
    "Cow" : "gae" , 
    "Buffalo" : "Bhens" ,
    "Breed" : "nassal"
}

user_input = input("Enter the words you want to print the urdu translation with")
print(infrormation_dictionary[user_input])
