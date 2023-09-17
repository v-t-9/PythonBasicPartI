import os
from ex63 import abs_path
#Write a Python program to check whether a file path is a file or a directory.
def file_or_directory(p):
    if os.path.isdir(p):
        return f"{p} is a directory"
    if os.path.isfile(p):
        return f"{p} is a file"

if __name__ == "__main__":
    path = abs_path("ex85.py")
    path2 = os.getcwd()
    print(file_or_directory(path))
    print(file_or_directory(path2))
