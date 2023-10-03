# Write a Python program to convert true to 1 and false to 0.
convert_true = lambda v: int(v == "True")

if __name__ == "__main__":
    a = "True"
    b = 1234
    print(convert_true(a))
    print(convert_true(b))