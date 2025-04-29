# Create a dictionary in such a way that have 4 name as the keys and the favorite languages as the values 
# assumes that the names must be unique 
# if a name used for once and then if used again with an updated value what will happen?


this_dictionary = {}

user_input_1 = input("Enter your name: ")
user_input_2 = input("Enter your favorite language: ")
this_dictionary.update({user_input_1:user_input_2})

user_input_1 = input("Enter your name: ")
user_input_2 = input("Enter your favorite language: ")
this_dictionary.update({user_input_1:user_input_2})

user_input_1 = input("Enter your name: ")
user_input_2 = input("Enter your favorite language: ")
this_dictionary.update({user_input_1:user_input_2})

user_input_1 = input("Enter your name: ")
user_input_2 = input("Enter your favorite language: ")
this_dictionary.update({user_input_1:user_input_2})

print(this_dictionary)

# nothing just the keys value gets updated nothing more then this
