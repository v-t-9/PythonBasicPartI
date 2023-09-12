# Write a Python program to calculate the body mass index.

bmi = lambda h, w: w/(h**2)

if __name__ == "__main__":
    he = float(input("Enter your height: "))
    we = float(input("Enter your weight:"))
    print("Your body mass index is: ", bmi(he,we))