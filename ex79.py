import sys
# Write a Python program to get the size of an object in bytes.

def obj_size(o):
    return f"The size of {o} is {sys.getsizeof(o)} bytes"
if __name__ == "__main__":
    s = "Hello"
    n = 987655543454665
    l = [12, "green", 45556, "red", "orange", 12234, "yellow"]
    print(obj_size(s))
    print(obj_size(n))
    print(obj_size(l))
