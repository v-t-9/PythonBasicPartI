# Write a Python program to determine if a variable is defined or not.

if __name__ == "__main__":
    try:
        s = "Hello"
    except NameError:
        print("Not defined.")
    else:
        print("Defined.")