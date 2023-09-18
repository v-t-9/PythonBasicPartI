# Write a Python program to check whether a string is numeric.
def is_numeric(s):
    if s.isnumeric() == True:
        return f"The string is numeric"
    else:
        return f"The string isn't numeric"

if __name__ == "__main__":
    s1 = "hello"
    s2 = "123"
    s3 = "1a2b3c"
    print(is_numeric(s1))
    print(is_numeric(s2))
    print(is_numeric(s3))