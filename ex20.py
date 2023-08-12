# Write a Python program that returns a string that is n (non-negative integer) 
# copies of a given string.

copies_string = lambda s,n: s*n
if __name__ == "__main__":
    s = "Hello"
    n1 = 5
    n2 = 6
    print(copies_string(s,n1))
    print(copies_string(s, n2))