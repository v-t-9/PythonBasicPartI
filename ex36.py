# Write a Python program to add two objects if both objects are integers.

def sum_of_objects(v1,v2):
    if isinstance(v1,int) == True and isinstance(v2, int) == True:
        return v1 + v2
    
if __name__ == "__main__":
    v1 = 12
    v2 = 3
    print(sum_of_objects(v1, v2))