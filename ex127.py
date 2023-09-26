# Write a Python program to check whether an integer fits in 64 bits.

int_64 = lambda n: n.bit_length() <=63
if __name__ == "__main__":
    n = 214748365178953568856336
    print(int_64(n))