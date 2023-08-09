import math
# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504


circle_area = lambda r: r**2*math.pi

if __name__ == "__main__":
    rad = float(input("Enter the radius of a circle: "))
    print("The area of the circle is: ", circle_area(rad))
