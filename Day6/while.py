# While loops

# For loops complete a sequence until a condition is met
# 1. list of items that we loop through and do something with each item
list_of_items = []
for item in list_of_items:
    Do something to each item

# 2. range of numbers where we execute the conditions once per number in the range
for number in range(1, 5):
    print(number)

# While loops are different bc they set
while something_is_true:
    Do something repeatedly
##################################################################

# Program a robot to jump 6 hurdles
# Create fake function and use a while loop to run the function once for each hurdle


def hurdle():
    Code to
    Jump over
    hurdle


number_of_hurdles = 6

while number_of_hurdles > 0:
    hurdle()
    number_of_hurdles -= 1


###########################################################################################################
# If we dont know the number of hurdles before the finish line:
# We can still set a condition that tells the while loop to end when the robot reaches the finish line

at_finish_line = False

while at_finish_line == False:
    hurdle()

# We can also write this as
while not at_finish_line:
    hurdle()
