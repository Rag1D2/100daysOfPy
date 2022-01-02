# Produce a Hangman game
import random
# 1. generate a random word
random_words = ["python", "microsoft", "apple",
                "android", "computer", "keyboard", ]
chosen_word = list(random.choice(random_words))
print(chosen_word)

# 2. Generate all letters in word as blank spaces
# for letter in chosen_word:

# 3. Ask user to guess a letter
# 4. Check if guessed letter is in the word
# 4a. If yes, replace blank space with letter
# (1). Are all blanks filled?
# (1a) If yes, player wins! Game Over!
# (1b) If no, return to step 3.
# 4b. If no, player loses a life
# (1) Are all lives gone?
# (1a) If yes, player loses! Game Over!
# (1b) If no, return to step 3.

# Input asking for a guess (letter)
#guess = input("Guess a letter ")

# Check letters in random word to see if they match
# If guessed letter is in game word, letter appears on screen in proper place
# If letter is not in game word, a step in the hangman picture is added
# Player wins if they guess all letters in the game word before hangman is complete
# Player loses if hangman is complete before all letters in game word are guessed
