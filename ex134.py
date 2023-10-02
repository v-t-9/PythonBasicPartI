# Write a Python program to input two integers on a single line.

if __name__ == "__main__":
    a,b = input("Enter 2 numbers:").split()
    print("Number 1:", int(a))
    print("Number 2:", int(b))