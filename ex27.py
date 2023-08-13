# Write a Python program that concatenates all elements in a list into a string and returns it.

def list_to_string(l):
    s = " "
    for i in l:
        if i != int:
            s = s + str(i)
        else:
            s = s + i
    return s
if __name__ == "__main__":
    l1 = ["a",1,"b",2,"c",3,"d",4]
    print(list_to_string(l1))