import os.path
# Write a Python program to retrieve the path and name of the file currently being executed.

def path_name():
    path = os.path.abspath(__file__)
    name = os.path.abspath(__name__)

    return F"Path: {path}\nName: {name}"

if __name__ == "__main__":
    print(path_name())