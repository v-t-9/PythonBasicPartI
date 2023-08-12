# Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference.

def greater_than_17(n):
    if n >17:
        return (n-17)*2
    else:
        return abs(n-17)
if __name__ == "__main__":
    n1 = 10
    n2 = 25
    print(greater_than_17(n1))
    print(greater_than_17(n2))