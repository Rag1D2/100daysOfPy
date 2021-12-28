# Data Types

# String

print("Hello"[0])
# H

print("Hello"[4])
# o

# Integers

print("123" + "456")
# 123456

print(123 + 456)
# 579


# Float
34.456

# Boolean
True
False


# Type Conversion
num_char = len(input("What is your name? "))  # Angela
print("Your name has " + num_char + " characters.")
# This throws a TypeError (cannot concat ints)


# type checking
print(type(num_char))
# class 'int'


# type conversion
num_char = len(input("What is your name? "))  # Angela
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
# Your name has 6 characters.


str()
float()
int()


a = float(123)
print(type(a))  # int
