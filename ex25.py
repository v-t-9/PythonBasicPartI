# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def has_value(v,l):
    if v in l:
        return True
    else:
        return False

if __name__ == "__main__":
    val1 = 3
    l = [1, 5, 8, 3]
    val2 = -1
    print(has_value(val1,l))
    print(has_value(val2,l))

    