# this project takes the guess of the user and then matches it accordingly 

import random 
n = random.randint(1,10)
guesses = 1
user_input= -1
while(user_input != n ):
    user_input = int(input("Enter your guessed number! "))
    if (user_input > n):
        print("Try Again! Guess lower number")
        guesses+=1
    elif (user_input < n):
        print("Try Again! Guess higher number")
        guesses+=1

print(f"You have guessed the number {n} for the {guesses} number of times correctly!")

