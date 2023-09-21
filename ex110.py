# Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
div_by_15 = lambda l: [i for i in l if i%15 ==0 ]
if __name__ == "__main__":
    l = [14, 15, 30, 35, 75, 90, 120, 125]
    print(div_by_15(l))
    