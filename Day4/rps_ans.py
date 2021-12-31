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

game_art = [rock, paper, scissors]
################################################################

# GAME LOGIC

comp_number = random.randint(0, 2)
weapon = ["Rock", "Paper", "Scissors"]

comp_choice = weapon[comp_number]

player_number = int(input(
    "Welcome to Rock, Paper, Scissors.\n Please Select a Choice: 0 for Rock, 1 for Paper or 2 for Scissors "))

player_choice = weapon[player_number]

# Player Choice
if player_choice == weapon[player_number]:
    print(f"Player Chose: {weapon[player_number]}\n{game_art[player_number]}")


# Computer Choice
if comp_choice == weapon[comp_number]:
    print(f"Computer Chose: {weapon[comp_number]}\n{game_art[comp_number]}")


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
