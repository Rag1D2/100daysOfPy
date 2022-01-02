# Functions
# Functions are identified by their name and () at the end.
print("Hello, World")

# Python has many built in functions, but we can also define our own


def my_function():
    # Do this
    # Then do this
    # Finally, do this


my_function()

# Indentation
# We use indentation to signal that the python command is inside of a function, loop, etc.


def hello():
    print("Hello")


hello()
print("World")

# See the levels of indentation in the below example?
# The if statement is inside of the function so the conditions of the if statement are indented inside opf the if statement which is inside of the function


def weather():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy":
        print("grey")
    print("Hello")


print("World")
