# Python Dictionaries
# Dictionaries are set as {key: value} pairs

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

'''
Here, we see that "Bug" and "Function" are the {Keys}, and the definitions that follow are the {Values}
Separate multiples and always end your list of k:v pairs with a comma (,)
'''
# How do we call on info from our dictionary?
print(programming_dictionary["Bug"])
# This will print the definition (value) that we paired with the key, "Bug"

# To add data into a dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
# This takes the existing dictionary, listed above, and removes all k:v pairs

# Edit an item in a dictionary
programming_dictionary["Bug"] = "# PUT NEW VALUE HERE TO EDIT THE DEFINITION OF BUG"

# Loop through a dictionary
for item in programming_dictionary:
    # This prints the key of each item
    print(item)

    # this prints the value of each item
    print(programming_dictionary[item])
