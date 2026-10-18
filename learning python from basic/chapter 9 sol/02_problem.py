import random

def game():
    print("You are playing the game!")
    score=random.randint(1,100)

    with open("Highscore.txt") as f:
        highscore=f.read()
    
    print(f"Your score: {score}")
    if(score>highscore or highscore==0):
        f.update(highscore)

game()