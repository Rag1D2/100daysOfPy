# Input age in years
# Calculate age in days, weeks and months
# Calculate how may days, weeks, months until 90 years old

age = int(input("How old are you? "))

til_ninety = 90 - age

days = til_ninety * 365
weeks = til_ninety * 52
months = til_ninety * 12


print(
    f"You have {days} days, {weeks} weeks, and {months} months until you are 90 years old")
