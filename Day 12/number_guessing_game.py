import random

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 to 100.")

attemps = 0
number = random.randint(1,100)

dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if dificulty == 'easy':
    attemps += 10
    while attemps != 0:
        print(f"You have {attemps} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        if guess == number:
            print(f"Yay! You guessed the number with {attemps} remaining!")
            break
        elif guess > number:
            print("Go Low!")
            print("Guess again.")
            attemps -= 1
        else:
            print("Go High!")
            print("Guess again.")
            attemps -= 1
else:
    attemps += 5
    while attemps != 0:
        print(f"You have {attemps} attempts remaining to guess the number.")
        guess = int(input("Guess the number: "))
        if guess == number:
            print(f"Yay! You guessed the number with {attemps} remaining!")
            break
        elif guess > number:
            print("Go Low!")
            print("Guess again.")
            attemps -= 1
        else:
            print("Go High!")
            print("Guess again.")
            attemps -= 1
    print(f"The number was {number}")