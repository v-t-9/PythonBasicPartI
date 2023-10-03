#  Write a Python program to check whether a variable is an integer or string.
def int_or_str(v):
    if type(v) is int:
        return f"Variable is a integer"
    if type(v) is str:
        return f"Variable is a string"
    
if __name__ == "__main__":
    a = 11
    b = "11"
    print(int_or_str(a))
    print(int_or_str(b))
