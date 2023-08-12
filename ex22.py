# Write a Python program to count the number 4 in a given list.

def count_4(l):
    c = 0
    for i in l:
        if i == 4:
            c = c + 1
    return c
if __name__ == "__main__":
    l1 = [4 ,3, 4, 9, 1, 4]
    l2 = [4, 3, 5, 6]
    print(count_4(l1))
    print(count_4(l2))
