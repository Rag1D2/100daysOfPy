# Create a choose your own adventure game using only if/elif/else statements
# At least 2 stages must exist
# At least 2 conditions per stage, all choices except one in each stage lead to "game over"

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

choice1 = input("You wake up on the shore of a lake. You have no memory of how you got here and have no idea what to do.\n You notice a small shack to your left and the lake to your right.\n In which direction do you go?").lower()

if choice1 == "right":
    print("You walk to the edge of the river and are stung almost immediately by a murder hornet! You are dead. GAME OVER")
elif choice1 == "left":
    choice2 = input(
        "You enter the front door of the small shack to find three doors. Each leads to a different room.\n Do you choose the Red, Yellow, or Green door?").lower()
else:
    print("Not a valid selection")

if choice2 == "red":
    print("Upon opening the door to the left, a giant explosion occurs and you are blown into 1 million pieces. You are dead. GAME OVER")
elif choice2 == "yellow":
    print("You step towards the middle door. As you approach, you trip on a small rug, stumble forward and smash your head on the door handle. You bleed to death while unconcious. You are dead. GAME OVER")
elif choice2 == "green":
    print("You open the door to the right. Revealing an open treasure chest filled with gold, silver and priceless stones!!!")
    print("CONGRATULATIONS YOU WIN")
else:
    print("Invalid Input")
