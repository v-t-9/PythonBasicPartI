# Write a Python program to filter positive numbers from a list.

positive_num = lambda x: x > 0
if __name__ == "__main__":
    l = [1,-1,22, -3,45,55,-87]
    pos = filter(positive_num, l)
    print(list(pos))