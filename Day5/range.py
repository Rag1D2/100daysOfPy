# Range Loops

# FYI for range to print "100" we must set the number to 101
# for number in range(1, 101):
# print(number)


# Calculate sum of all even numbers in range from 1, 100
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)
