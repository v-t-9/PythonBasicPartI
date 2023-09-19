# Write a Python program to get the ASCII value of a character.

ascii_value = lambda c: ord(c)
if __name__ == "__main__":
    ch = input("Enter a character: ")
    print("The ASCII value of the character " , ch , "is: " , ascii_value(ch))