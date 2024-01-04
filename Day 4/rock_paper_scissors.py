import random
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

choices = ["Rock","Paper","Scissors"]

upper_choice = len(choices) - 1
computer_choice = random.randint(0,2)



if user_choice == "0" and choices[computer_choice] == "Scissors":
    print("You Won")
elif user_choice == "0" and choices[computer_choice] == "Rock":
    print("It's a tie")
elif user_choice == "1" and choices[computer_choice] == "Rock":
    print("You Won")
elif user_choice == "1" and choices[computer_choice] == "Paper":
    print("It's a  tie")
elif user_choice == "2" and choices[computer_choice] == "Paper":
    print("You Won!")
elif user_choice == "2" and choices[computer_choice] == "Scissors":
    print("It's a tie")
else:
    print("You lost")
