# Produce a Hangman game

# import modules
import random
from hangman_art import logo, stages
lives = 6

print(f"WELCOME TO \n {logo}")
# 1. generate a random word
word_list = ["python", "microsoft", "mouse",
             "android", "computer", "keyboard"]
chosen_word = random.choice(word_list)

# 2. Generate all letters in word as blank spaces
display = []
word_length = len(chosen_word)

for letter in chosen_word:
    display += "_"
print(display)

# Initialize game
end_of_game = False

while end_of_game == False:
    # 3. Ask user to guess a letter
    guess = input("Guess a letter: ").lower()
    # 4. Check if guessed letter is in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        # 4a. If yes, replace blank space with letter
        if guess == letter:
            print("Correct!")
            display[position] = letter
            print(display)
    # 4b. If no, player loses a life
    if guess not in chosen_word:
        lives -= 1
        print(f"WRONG!\n You have {lives} chances left")
        print(stages[lives])
        print(display)
        # (1) Are all lives gone?
        if lives == 0:
            # (1a) If yes, player loses! Game Over!
            end_of_game = True
            print("YOU LOSE! Sorry to leave you hanging!")

    # (1). Are all blanks filled?
    if "_" not in display:
        # (1a) If yes, player wins! Game Over!
        end_of_game = True
        print("YOU WIN!")
