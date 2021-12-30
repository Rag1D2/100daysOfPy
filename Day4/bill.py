# Who will pay the bill? PLay bill roulette to find out!
import random

number = random.randint(0, 4)
people = ["Angela", "Dwight", "Kevin", "Pam", "Jim"]

print(f"The person paying the bill tonight is: {people[number]}")
