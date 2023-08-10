# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

def list_tuple_generation(n):
    l = n.split(",")
    t = tuple(l)
    return f"The list is {l}, and the tuple is {t}"

if __name__ == "__main__":
    nums = input("Please enter some comma separated numbers ")
    print(list_tuple_generation(nums))



