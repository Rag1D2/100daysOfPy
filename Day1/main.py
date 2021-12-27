# Comments look like this

# Print() prints whatever you enter into the parantheses to the console
print("Hello World")

# Using \n prints everything after is on a new line
print("Hello World!\nHello World!!!")

# Strings are a data type in python
# Strings can be concatenated using '+'

print("Hello" + "Angela")
# "HelloAngela"

print("Hello" + " " + "Angela")
# Hello Angela

# INPUT prompts the user for information. This data can then be used in our code.

# User types their name
nameLength = len(input("What is your name?"))
# len takes the input and counts the number of characters in the input provided by the user
print(nameLength)
# if name is "Angela" console should print '6'

# We can also do this entire thing in one line
print(len(input("What is your name? ")))
