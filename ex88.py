# Given variables x=30 and y=20, write a Python program to print "30+20=50".

sum_num = lambda a,b: a + b

if __name__ == "__main__":
    x = 30
    y = 20
    print("30 + 20 =" ,sum_num(x,y))