# Write a Python program to sort three integers without using conditional statements and loops.

def sort_3_int(n1,n2,n3):

    n = [n1,n2, n3]
    return f"The numbers in sorted order: {sorted(n)}"


if __name__ =="__main__":
    a = int(input("Enter a number: " ))
    b = int(input("Enter a number: " ))
    c = int(input("Enter a number: " ))
    
    print(sort_3_int(a,b,c))