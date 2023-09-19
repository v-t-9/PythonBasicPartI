 # Write a Python program to test whether all numbers in a list are greater than a certain number.

def greater_than_n(n,l):
    res = []
    for i in l:
        if i >100:
            res.append(True)
        else:
            res.append(False)
    return all(res)

if __name__ == "__main__":
    n = 100
    l1 = [21, 44, 123, 456, 8]
    l2 = [345, 123, 456, 876, 1022]
    print(greater_than_n(n,l1))
    print(greater_than_n(n,l2))
