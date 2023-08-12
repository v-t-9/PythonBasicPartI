# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def within_100(n):
    if abs(1000 - n) <=100 or abs(2000 - n) <=100:
        return True
    else:
        return False
if __name__ == "__main__":
    n1 = 1015
    n2 = 1100
    n3 = 2015
    n4 = 2300
    n5 = 500
    print(within_100(n1))
    print(within_100(n2))
    print(within_100(n3))
    print(within_100(n4))
    print(within_100(n5))
