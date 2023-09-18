# Write a Python program to create a copy of its own source code.

def copy_source():
    with open(__file__) as f:
        return f.read()
    
if __name__ == "__main__":
    print(copy_source())