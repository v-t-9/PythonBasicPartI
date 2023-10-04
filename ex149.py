# Write a Python function that takes a positive integer and returns the sum of the cube of all positive integers smaller than the specified number.

def cube_smaller_n(n):
    s = 0
    for i in range(1, n):
        s = s + i**3

    return s

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print(cube_smaller_n(n))