# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

def list_diff(s1,s2):
    res = set()
    for i in s1:
        if i not in s2:
            res.add(i)
    return res

if __name__ == "__main__":
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(list_diff(color_list_1, color_list_2))