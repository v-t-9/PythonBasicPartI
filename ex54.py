import os
# Write a Python program to get the current username.

def current_username():
    return os.getlogin()
if __name__ == "__main__":
    print(current_username())