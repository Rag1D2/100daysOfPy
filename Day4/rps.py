# My solution to the RPS code challenge

# Randomization and Python Lists
import random

# Game Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

## GAME LOGIC ##

# Player prompt
player_choice = input(
    "Welcome to Rock, Paper, Scissors.\n Please Select a Choice: Rock, Paper or Scissors ").lower()

# Computer Logic
comp_choice = random.randint(0, 2)


# Player Choice
if player_choice == "rock":
    player_choice = 0
    print(f"Player Chose: Rock\n{rock}")
elif player_choice == "paper":
    player_choice = 1
    print(f"Player Chose: Paper\n{paper}")
elif player_choice == "scissors":
    player_choice = 2
    print(f"Player Chose: Scissors\n{scissors}")

# Computer Choice
if comp_choice == 0:
    print(f"Computer Chose: Rock\n{rock}")
elif comp_choice == 1:
    print(f"Computer Chose: Paper\n{paper}")
elif comp_choice == 2:
    print(f"Computer Chose: Scissors\n{scissors}")

# Game Conditions
if player_choice == comp_choice:
    print("It is a tie!")
elif player_choice == 0 and comp_choice == 2:
    print("YOU WIN!")
elif player_choice == 1 and comp_choice == 0:
    print("YOU WIN!")
elif player_choice == 2 and comp_choice == 1:
    print("YOU WIN!")
else:
    print("You LOSE!")
