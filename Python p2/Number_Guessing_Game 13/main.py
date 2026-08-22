import random

number = random.randint(1, 100)
user_guess = -1
guesses = 0
while user_guess != number:
    guesses += 1
    user_guess = int(input("Enter the number:"))
    if user_guess < number:
        print("Enter higher number please:")
    elif user_guess > number:
        print("Enter lower number please:")
print(f"Congrats! you guessed the number {number} in {guesses} attempts")
