# Write a Python program to convert the distance (in feet) to inches, yards, and miles.
def distance_converter(ft):
    inches = ft*12
    yards = ft/3
    miles = ft/5280
    
    return f"The distance entered is equivalent to {inches} inches or {yards} yards or {miles} miles. "

if __name__ == "__main__":
    ft = int(input("Enter distance in feet: " ))
    print(distance_converter(ft))