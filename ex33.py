# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
def sum_of_three(n1, n2, n3):
    res = 0
    if n1 == n2 or n1 == n3 or n2 == n3:
        res = 0
        return f"The result is {res}"
    
    res = res + n1 + n2 + n3 

    return f"The result is {res}"
    

if __name__ == "__main__":
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a second number: "))
    n3 = int(input("Enter a third number: "))
    print(sum_of_three(n1, n2, n3))