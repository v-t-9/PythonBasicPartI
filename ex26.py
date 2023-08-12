# Write a Python program to create a histogram from a given list of integers.

def histogram(l,ch):
    r = ""
    for i in l:
        r = r + ch*i + "\n"
    return r
if __name__ == "__main__":
    l1 = [3,5,7,1,4]
    l2 = [8,4,3,2,2,8]
    ch = "*"
    print(histogram(l1,ch))
    print(histogram(l2, ch))