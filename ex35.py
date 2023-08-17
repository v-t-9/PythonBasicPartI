# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5
def equal_or_five(n1, n2):
    if n1 == n2:
        return True
    elif abs(n1 - n2) == 5:
        return True
    elif n1 + n2 == 5:
        return True
    else:
        return False
if __name__ == "__main__":
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter a second number: "))
    print(equal_or_five(n1, n2))