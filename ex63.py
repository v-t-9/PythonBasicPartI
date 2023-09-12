import os
# Write a Python program to get an absolute file path.

abs_path = lambda f: os.path.abspath(f)

if __name__ == "__main__":
    print(abs_path("test.txt"))