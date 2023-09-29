# Write a Python program to add leading zeroes to a string.

def add_zeros(s):
    res = s.zfill(len(s)+3).ljust((len(s)+6),"0")
    return res

if __name__ == "__main__":
    s = "Hello"
    print(add_zeros(s))