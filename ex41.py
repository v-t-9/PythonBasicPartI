import os.path
# Write a Python program to check whether a file exists.
 
def check_file(st):
    if os.path.exists(st):
        return f"The file exists."
    else:
        return f"The file cannot be found."
if __name__ == "__main__":
    print(check_file("text.txt"))