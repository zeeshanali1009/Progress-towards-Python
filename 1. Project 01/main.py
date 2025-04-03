# Here we are trying to build a game snake , water and gun based game 
# Water = -1   also acts as the computer 
# snake = 1
# Gun = 0
import random
computer = random.choice([0,1,-1])
yourchoice = input("Enter your choice : ")
game_dictionary = { "S": 1, "W": -1 , "G": 0}
reversed_dictionary = {1 : "S", -1: "W" , 0 : "G"}
you = game_dictionary[yourchoice]
print(f"You choose {reversed_dictionary[you]}\nComputer choosed {reversed_dictionary[computer]}")

if (you == computer):
    print("It's a draw!")
else:
    if(computer == -1 and you == 0):
        print("You loose!")
    elif(computer == -1 and you == 1):
        print("You win!")
    elif(computer == 1 and you == -1):
        print("You loose!")
    elif(computer == 1 and you == 0):
        print("You win!") 
    elif(computer == 0 and you == -1):
        print("You win!")
    else:
        print("Something went wrong!")

# So, that was our first program to be used as the game development program in fact first one to develope
# a real time game

