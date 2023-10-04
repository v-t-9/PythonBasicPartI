# Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.
def odd_product(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] != l[j]:
                if l[i] * l[j] == 0:
                    return False
                else:
                    if (l[i] * l[j]) in l:
                        return True
                    else:
                        return False
        
if __name__ == "__main__":
    l1 = [28, 34, 15, 5, 67, 8]
    l2 = [1, 6, 4, 7, 8]
    l3 = [1, 3, 5, 7, 9]
    print(odd_product(l1))
    print(odd_product(l2))
    print(odd_product(l3))