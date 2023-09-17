# Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.

def first_day_of_month(a):
    if a ==1:
        return f"First day of a Month!"

if __name__ == "__main__":
    v = 1
    print(first_day_of_month(v))