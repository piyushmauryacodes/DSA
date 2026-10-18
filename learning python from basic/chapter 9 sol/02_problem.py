import random

def game():
    print("You are playing the game!")
    score=random.randint(1,100)

    with open("Highscore.txt","r") as f:
        highscore=f.read()
        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0
            # with open("Highscore.txt","w") as file:
            #     print("The file is updated with 0")
            #     file.write("0")
    print(f"Your score: {score}")
    if (score>highscore):
        with open("Highscore.txt","w") as f:
            f.write(str(score))
    return 

game()