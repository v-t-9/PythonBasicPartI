# Write a Python program that computes the greatest common divisor (GCD) of two positive integers.


def gdc(n1, n2):
    if n1 > n2:
        a = n1
        b = n2
    else:
        a = n2
        b = n1

    while b !=0:
        r = a%b
        if r == 0:
            return b
        a = b
        b = r

if __name__ == "__main__":
    n1 = 336
    n2 = 360
    print(gdc(n1,n2))