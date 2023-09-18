# Write a Python program to get the Identity, Type, and Value of an object.

def id_type_value_obj(o):
    return f"Identity: {id(o)}\nType: {type(o)}\nValue: {o}"


if __name__ == "__main__":
    o = [1, "a", 2, "b", 3, "c"]
    print(id_type_value_obj(o))
