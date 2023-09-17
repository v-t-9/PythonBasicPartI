#  Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary).
sum_items = lambda a: sum(list(a))

if __name__ == "__main__":
    l = [4,56,25,80]
    t = (55,21,68)
    print(sum_items(l))
    print(sum_items(t))
