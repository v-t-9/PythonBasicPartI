#Write a Python program to calculate the hypotenuse of a right angled triangle.

def hypotenuse(a,b):
    h = ((a**2) + (b**2))**(1/2)
    return h

if __name__ == "__main__":
    a = int(input("Enter one side of the triangle:"))
    b = int(input("Enter one side of the triangle:"))
    print(hypotenuse(a,b))