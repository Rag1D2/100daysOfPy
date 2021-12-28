# MATH
3 + 5  # 8

7 - 4  # 3

3 * 2  # 6

6 / 3  # 2.0 (division produces a float by default)

3 ** 2  # 9 (exponent)

# Python math follows order fo operations
PEMDAS
()
**
*
/
+
-


# Rounding numbers
8 / 3 = 2.6666666666666665

print(round(8 / 3))  # Round will round the output to the nearest whole number
# 3


print(8 / 3, 2)  # The second argument tells us how many decimal places to round to
# 2.67

# This is called floor division: result automatically rounded to nearest whole number
print(8 // 3)
# 3


# F-String
score = 0
height = 1.8
isWinning = True
# how do we get these different types to all represent in a string together?

print(
    f"your score is {score}, you are {height} meters tall and it is {isWinning}, you are winning")
