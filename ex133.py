import datetime
# Write a Python program to calculate the time runs (difference between start and current time) of a program
def mul_num(n):
    l = [i*2 if i%2==0 else i*3 for i in range(n) ]
    return l
if __name__ == "__main__":
    time_s = datetime.datetime.now()
    n = 5000
    print(mul_num(n))
    time_f = datetime.datetime.now()
    t = str(time_f-time_s).split(":")
    print("Time run: ", t[2])