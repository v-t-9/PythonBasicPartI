# Write a Python program to check whether multiple variables have the same value.
same_value = lambda a,b,c: a == b == c
if __name__ == "__main__":
    a = 1
    b = 1 
    c = 1
    d = 2
    print(same_value(a,b,c))
    print(same_value(a,b,d))