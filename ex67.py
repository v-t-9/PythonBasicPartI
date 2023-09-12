# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

def convert_pressure(p):
    pounds = p/6.895
    mer = p*7.50062
    ap = p/101.5

    return f"Pounds per sqare inch: {pounds}.\nMillimeter of mercury (mmHg): {mer}.\nAtmosphere pressure: {ap}"

if __name__ =="__main__":
    pr = float(input("Enter pressure in kilopascals: "))
    print(convert_pressure(pr))