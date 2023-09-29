import os
# Write a Python program to list the home directory without an absolute path.

if __name__ == "__main__":
    print(os.path.expanduser("~"))