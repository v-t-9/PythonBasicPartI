# Write a Python program to calculate sum of digits of a number.
def sum_digits(n):
    num_l = [int(i) for i in n]
    return sum(num_l)


if __name__ =="__main__":
    num = input("Enter number: ")
    print(sum_digits(num))