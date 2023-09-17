import os
# Write a Python program to get the size of a file.
size_file = lambda f: os.path.getsize(f)

if __name__ == "__main__":
    file = "ex86.py"
    print("The size of ", file, "is: ", size_file(file), "bytes.")