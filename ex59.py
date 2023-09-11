# Write a Python program to convert height (in feet and inches) to centimeters.

def height_converter_ft_in_to_cm(h):
    he = h.split(" ")
    he1 = [int(i) for i in he]
    h_ft = he1[0]*30.48
    h_in = he1[1]*2.54
    h_cm = h_ft + h_in
    return f"Your height in centimeters is: {h_cm}"

# def height_converter_cm_to_ft_in(h):
#     h_in = float(h)/2.54
#     h_ft = h_in/12
#     return f"Your height in feet and inches is {h_ft} feet or {h_in} inches"

if __name__ == "__main__":
    h1 = input("Enter your height in feet and inches: " )
    print(height_converter_ft_in_to_cm(h1))
    # h1 = input("Enter your height in centimeters: " )
    # print(height_converter_cm_to_ft_in(h1))
