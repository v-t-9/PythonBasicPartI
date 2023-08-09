# Write a Python program that accepts the user's first and last name and prints them 
# in reverse order with a space between them.

last_first_name = lambda first_name, last_name: last_name + ", " + first_name

if __name__ == "__main__":
    first_name = input("Please, enter your first name: ")
    last_name = input("Please, enter your last name: ")
    print(last_first_name(first_name, last_name))