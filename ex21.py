# Write a Python program that determines whether a given number (accepted from the 
# user) is even or odd, and prints an appropriate message to the user.

def even_odd(n):
    if n % 2 == 0:
        return f"The number {n} is even."
    return f"The number {n} is odd."

if __name__ == "__main__":
    num = int(input("Write a number: " ))
    print(even_odd(num))
    