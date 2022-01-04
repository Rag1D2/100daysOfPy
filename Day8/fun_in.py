# Function Inputs

# create the function
def call_me():
    print("Hello")  # Do Something
    print("Welcome")  # Do Something Else
    print("Today")  # Do one more thing


# call the function to execute the code inside
call_me()

# Now add a variable that takes in a users name and runs the greet function with the users name included

name = input("What is you name? ")


def greet(name):
    print(f"Hello {name}")
    print("How are you?")


greet(name)
