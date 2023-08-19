import time
# Write a Python program to get the execution time of a Python method.

def ex_time(l):
    start = time.time()
    x = append_sort_list(l)
    end = time.time()
    return end - start

def append_sort_list(l):
    for i in range(100, 1000000, 2):
        l.append(i)
    return sorted(l)

if __name__ == "__main__":
    l = [5,4,9,2,345,8765,2334,4,23456,1,20]
    print(ex_time(l))