# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

def value_sum(n):
    res = 0
    res = res + n + int(str(n)*2) + int(str(n)*3)
    return res


if __name__ == "__main__":
    n= 5
    print(value_sum(n))