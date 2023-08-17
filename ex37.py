# Write a Python program that displays your name, age, and address on three different lines.
personal_data= lambda na, ag,ad: "Your name is " + na +"\nYour age is " + ag+ "\nYour address is " + ad

if __name__ == "__main__":
     name = input("Write your name: ")
     age = input("Write your age: ")
     address = input("Write your address: ")
     print(personal_data(name, age, address))