import random


def game():
    print("You are Playing a Game!")
    score = random.randint(1, 50)
    print(f"You scored {score}")
    with open("chapter 09/08_File.txt", "r") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    if score > hiscore:
        with open("chapter 09/08_File.txt", "w") as f:
            f.write(str(score))



game()
