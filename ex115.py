import functools
# Write a Python program to compute the product of a list of integers (without using a for loop).

product = lambda x,y: x*y

if __name__ =="__main__":
    l = [1,14,22,3,45,55,87]
    prod = functools.reduce(product,l)
    print(prod)