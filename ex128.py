#  Write a Python program to check whether lowercase letters exist in a string.

def lowercase_letters(s):
    for i in s:
        if i.islower():
            return True
    return False
if __name__ == "__main__":
    s1 = "Hello"
    s2 = "HELLO"
    print(lowercase_letters(s1))
    print(lowercase_letters(s2))