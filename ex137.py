# Write a Python program to extract a single key-value pair from a dictionary into variables.


if __name__ == "__main__":
    dic = {"1": "Apple"}
    [(k, v)] = dic.items()
    print(k)
    print(v)