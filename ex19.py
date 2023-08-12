# Write a Python program to get a newly-generated
# string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

def front_is(s):
    if s[:2] == "Is":
        return s
    else:
        return "Is " + s
if __name__ == "__main__":
    s1 = "Is Now"
    s2 = "Now"
    print(front_is(s1))
    print(front_is(s2))