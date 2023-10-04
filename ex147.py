# Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.

def divisible(a,b):
    if a % b == 0:
        t = "{} is divisible by {}".format(a,b)
        return t
    else:
        t = "{} isn't divisible by {}".format(a,b)
        return t


if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    print(divisible(a,b))