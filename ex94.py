# Write a Python program to convert the bytes in a given string to a list of integers.

bytes_to_list = lambda s: list(s)


if __name__ == "__main__":
     s = b'Abc'
     print(bytes_to_list(s))


