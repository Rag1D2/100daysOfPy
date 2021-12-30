# The "official" solution to the RPS challenge
import random

# GAME ART ############################
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
################################################################

# GAME LOGIC

comp_number = random.randint(0, 2)
weapon = ["Rock", "Paper", "Scissors"]

comp_choice = weapon[comp_number]

player_choice = weapon[int(input(
    "Welcome to Rock, Paper, Scissors.\n Please Select a Choice: 0 for Rock, 1 for Paper or 2 for Scissors "))]

# Player Choice
if player_choice == weapon[0]:
    print(f"Player Chose: Rock\n{rock}")
elif player_choice == weapon[1]:
    print(f"Player Chose: Paper\n{paper}")
elif player_choice == weapon[2]:
    print(f"Player Chose: Scissors\n{scissors}")

# Computer Choice
if comp_choice == weapon[0]:
    print(f"Computer Chose: Rock\n{rock}")
elif comp_choice == weapon[1]:
    print(f"Computer Chose: Paper\n{paper}")
elif comp_choice == weapon[2]:
    print(f"Computer Chose: Scissors\n{scissors}")

# Game Conditions
if player_choice == comp_choice:
    print("It is a tie!")
elif player_choice == weapon[0] and comp_choice == weapon[2]:
    print("YOU WIN!")
elif player_choice == weapon[1] and comp_choice == weapon[0]:
    print("YOU WIN!")
elif player_choice == weapon[2] and comp_choice == weapon[1]:
    print("YOU WIN!")
else:
    print("You LOSE!")
