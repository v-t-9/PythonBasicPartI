# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
def min_and_max(l):
    mi = l[0]
    ma = l[0]

    for i in l:
        if i >= ma:
            ma = i
        if i <= mi:
            mi = i
    res = "Maximum number: {}.\nMinimum number: {}. ".format(ma, mi)
    return res
if __name__ == "__main__":
    l = [28, 34, 15, 5, 67, 8]
    print(min_and_max(l))