# Build a tip calculator
# Takes input for total bill
# Divides bill by number of guests
# Prompts guest for a tip
# Outputs bill total plus desired tip

bill = float(input("How much was the bill? $"))
tip = int(input("How much of a tip would you like to leave? "))
guests = int(input("How many people are splitting the bill? "))
bill_with_tip = tip / 100 * bill + bill


billTotal = "{:.2f}".format(bill_with_tip)
myTotal = billTotal / guests

print(
    f"Your bill is ${bill}. You added a {tip}% so the total bill is ${bill_with_tip} tip. Your total is: ${myTotal}")
