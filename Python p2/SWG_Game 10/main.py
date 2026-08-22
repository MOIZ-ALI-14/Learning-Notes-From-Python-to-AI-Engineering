import random

print("\n*-* Most Welcome to Snake Water Gun Game *-*\n")


def mylogic():
    computer = random.choice([1, -1, 0])
    youstr = input('Enter your choice ("s","w","g"):')
    youdict = {"s": 1, "w": -1, "g": 0}
    reversedict = {1: "Snake", -1: "Water", 0: "Gun"}
    you = youdict[youstr]
    print(f"You entered {reversedict[you]}!\nComputer entered {reversedict[computer]}!")
    return computer, you


def main():
    computer, you = mylogic()
    if computer == you:
        print("It is a draw!")
    elif computer == -1 and you == 1:
        print("You Win!")
    elif computer == -1 and you == 0:
        print("You Lose!")
    elif computer == 1 and you == -1:
        print("You Lose!")
    elif computer == 1 and you == 0:
        print("You Win!")
    elif computer == 0 and you == -1:
        print("You Win!")
    elif computer == 0 and you == 1:
        print("You Lose!")
    else:
        print("Something Went Wrong!")


main()

while True:
    askques = input("do you want to play more? (yes/no): ")
    if askques == "yes":
        main()
    elif askques == "no":
        print("Good Bye Dear!")
        break
    else:
        print("You Crashed the Program Mental!")
        break
