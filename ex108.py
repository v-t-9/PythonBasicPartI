import os
from ex63 import abs_path
# Write a Python program to find the path to a file or directory when you encounter a path name.

if __name__ == "__main__":
    print(os.path.basename(abs_path("test.txt")))
    print(os.path.dirname(abs_path("test.txt")))
    