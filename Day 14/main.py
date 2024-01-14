import random
from game_data import data
from art import logo, vs

print(logo) # Displays the art.
score = 0 # Keep the score check.
choice_one = random.choice(data) # Picks a random account from fame_data.py file from the data dictionary.
is_True = True # Keeps hold that the condition remains true till the user is guessing the answer right.
while is_True: # Keep asking for the input while is_True is true.
    print(f"Compare A: {choice_one.get("name")},{choice_one.get("description")},{choice_one.get("country")}.")

    print(vs)

    choice_two = random.choice(data)
    print(f"Compare B: {choice_two.get("name")},{choice_two.get("description")},{choice_two.get("country")}.")

    choice = input("Which has more followers? Type 'A' or 'B': ")

    if choice == 'A':
        if choice_one.get("followers") > choice_two.get("followers"):
            score += 1
            print(f"Yay, your score is {score}")
        else:
            print(f"Oops, game over;( Your score is {score}")
            is_True = False
    else:
        if choice_two.get("followers") > choice_one.get("followers"):
            score += 1
            print(f"Yay, your score is {score}")
        else:
            print(f"Oops, game over;( Your score is {score}")
            is_True = False


