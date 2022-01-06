# Create a silent/secret auction program
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program")

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while not bidding_finished:
    name = input("What is you name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    other_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if other_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif other_bidders == "yes":
        cls()
