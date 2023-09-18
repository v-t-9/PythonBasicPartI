#  Write a Python program to swap two variables.
def swap_var(a,b):
    temp = a
    a = b
    return f"v1 = {a}\nv2 = {temp}"

if __name__ == "__main__":
    v1 = "x"
    v2 = "y"
    print("v1 = ",v1,"\nv2 =",v2)
    print(swap_var(v1,v2))
