# Create a function that takes in an input and checks if it is a prime number

n = int(input("Give us a number to check "))


def prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
    else:
        print("This is a prime number")


prime(n)
