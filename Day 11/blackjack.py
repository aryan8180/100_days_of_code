import random

logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
'''

cards = ["K", "Q", "J", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10]
face_card = {"K": 10, "Q": 10, "J": 10, "A": 11}

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if choice == 'y':
    print(logo)
    user_score = 0
    user_list = []
    
    first_card = random.choice(cards)
    if first_card in face_card:
        user_list.append(first_card)
        user_score += face_card[first_card]
    else:
        user_list.append(first_card)
        user_score += first_card

    second_card = random.choice(cards)
    if second_card in face_card:
        user_list.append(second_card)
        user_score += face_card[second_card]
    else:
        user_list.append(second_card)
        user_score += second_card

    print(f"Your card: {user_list}, current score: {user_score}")

    computer_score = 0
    computer_list = []

    first_computer = random.choice(cards)
    if first_computer in face_card:
        computer_list.append(first_computer)
        computer_score += face_card[first_computer]
    else:
        computer_list.append(first_computer)
        computer_score += first_computer
    
    second_computer = random.choice(cards)
    if second_computer in face_card:
        computer_list.append(second_computer)
        computer_score += face_card[second_computer]
    else:
        computer_list.append(second_computer)
        computer_score += second_computer
    
    print(f"Computer's first card: {computer_list}")
choice_again = input("Type 'y' to get another card, type 'n' to pass: ")
if choice_again == 'y':
    third_card = random.choice(cards)
    if third_card in face_card:
        user_list.append(third_card)
        user_score += face_card[third_card]
    else:
        user_list.append(second_card)
        user_score += third_card
    print(f"Your final hand: {user_list}, final score {user_score}")
    print(f"Computer's final hand: {computer_list}, final score: {computer_score}")

    if user_score > 21:
        print("You went over, you lose!")
    elif computer_score > 21 and user_score < 22:
        print("YOU WON!")
    elif user_score > computer_score:
        print("YOU WON!")
    elif computer_score > user_score:
        print("Not today;(")
    else:
        print("Draw")
else:
    if user_score > 21:
        print("You went over, you lose!")
    elif computer_score > 21 and user_score < 22:
        print("YOU WON!")
    elif user_score > computer_score:
        print("YOU WON!")
    else:
        print("Draw")