# Write a Python program to calculate the sum of three given numbers. 
# If the values are equal, return three times their sum.

def sum_numbers(n1, n2, n3):
    if n1 == n2 and n1 == n3:
        return (n1 +n2 + n3)*3
    return (n1 +n2 + n3)
if __name__ == "__main__":
    n1 = 10
    n2 = 25
    n3 = 60

    print(sum_numbers(n1, n2, n3))
    print(sum_numbers(n1, n1, n1))