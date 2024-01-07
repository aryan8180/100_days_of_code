import random 

list_of_words = ["mouse", "keyboard", "laptop", "xbox"]

computer_word_index = random.randint(0, len(list_of_words) - 1)
computer_word = list_of_words[computer_word_index]

guess_list = ["_" for _ in computer_word]
print(" ".join(guess_list))

while "_" in guess_list:
    guess = input("Enter your guess: ").lower()
    for i in range(len(computer_word)):
        if guess == computer_word[i]:
            guess_list[i] = guess
    print(" ".join(guess_list))

print("Congratulations! You guessed the word:", computer_word)
        
