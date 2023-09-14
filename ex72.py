import math
# Write a Python program to get the details of the math module.
def details(m):
    return dir(m)

if __name__ == "__main__":
    print(details(math))