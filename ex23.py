# Write a Python program to get n (non-negative integer) copies of the first 2 characters of 
# a given string. Return n copies of the whole string if the length is less than 2.

def string_copies(n,s):
    if len(s)<=2:
        return s*n
    else:
        return s[:2]*n

if __name__ == "__main__":
    n1 = 4
    s1 = "Hello"
    n2 = 3
    s2 = "I"
    print(string_copies(n1,s1))
    print(string_copies(n2,s2))
    