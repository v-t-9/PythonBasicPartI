import sys
# 2. Write a Python program to find out what version of Python you are using.
def version():
    return f"Version:", sys.version

if __name__ == "__main__":
    print(version())