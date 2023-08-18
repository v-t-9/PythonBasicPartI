# Write a Python program to print without a newline or space.

def without_newline_space(a,b):
    res = ""
    c = 0
    while c <10:
        res = res + a + b
        c = c + 1
    return res
        
if __name__ == "__main__":
    a = "Hello"
    b = "Goodbye"
    print(without_newline_space(a,b))