# Write a Python program to sum the first n positive integers.

def sum_n_positive(n):
    res = 0
    for i in range(n+1):
        res = res + i
    return res

if __name__ == "__main__":
    num = int(input("Enter a positive integer: "))
    print(sum_n_positive(num))

