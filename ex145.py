# Write a Python program to test if a variable is a list, tuple, or set.
def list_or_tup_or_set(v):
    if type(v) is list:
        return f"Variable is a list"
    if type(v) is tuple:
        return f"Variable is a tuple"
    if type(v) is set:
        return f"Variable is a set"
    
if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = (1, 2, 3, 4)
    c = {1, 2, 3, 4}
    print(list_or_tup_or_set(a))
    print(list_or_tup_or_set(b))
    print(list_or_tup_or_set(c))