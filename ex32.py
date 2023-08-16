from ex31 import gdc
# Write a Python program to find the least common multiple (LCM) of two positive integers


lcm = lambda n1, n2: (n1*n2)/gdc(n1,n2)

if __name__ == "__main__":
    n1 = 80
    n2 = 150
    print(lcm(n1, n2))