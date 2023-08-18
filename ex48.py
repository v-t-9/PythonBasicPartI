# Write a Python program to parse a string to float or integer.

def parse_str(st):
    fl = float(st)
    integ = int(fl)
    return f"Float: {fl}\nInt: {integ}"
if __name__ == "__main__":
    st = "4945.34567"
    print(parse_str(st))