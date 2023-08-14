# Write a Python program that will accept the base and height of a triangle  and compute its area.

area_triangle = lambda b,h: f"The area of the triangle is: {0.5*b*h}"

if __name__ == "__main__":
    base = float(input("Enter the base of a triangle: "))
    height = float(input("Enter the height of a triangle: "))
    print(area_triangle(base, height))