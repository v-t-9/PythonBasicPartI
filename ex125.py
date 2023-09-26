import collections
# Write a Python program to sum all counts in a collection.

if __name__ == "__main__":
    c = [1,2,2,4,55,6,77,8,9,-8,4]
    print(sum(collections.Counter(c).values()))
