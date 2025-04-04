# This program makes the game and takes the high score if the high score is f=greater then the existing 
# high score then replace it with higher score 
import random

def game ():
    print("You are playing the game...")
    score =  random.randint(10,100)
    with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/02._hiscore.txt') as f :
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore = int(hiscore)
        else:
            hiscore  = 0
    print(f"your score is : {score}")

    if (score > hiscore):
        with open('C:/Users/Zeeshan Ali/Desktop/Python-Learning-Course/9.9._Chapter 9 Practice/02._hiscore.txt' , 'w') as f:
            f.write(str(score))

    return score

game()
