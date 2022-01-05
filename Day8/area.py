import math
# Create a function that take in a width and height and returns the area of the room
# 1 can of paint covers 5 sq meters, determine how many cans of paint are needed to complete the job based on the area fo the room
length = int(input("What is the length of the room? "))
width = int(input("What is the width of the room? "))


def area(length, width):
    cans_needed = math.ceil((length * width) / 5)
    print(f"You need {cans_needed} cans of paint to complete this job")


area(length, width)
