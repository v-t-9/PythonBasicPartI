# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

def sum_of_two(n1, n2):
    res = n1 + n2
    if res >= 15 and res <= 20:
        return f"The result is {20}"
    
    
    return f"The result is {res}"
    


if __name__ == "__main__":
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a second number: "))
    print(sum_of_two(n1, n2))