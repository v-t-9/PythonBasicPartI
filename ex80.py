import sys
# Write a Python program to get the current value of the recursion limit.
def recursion_limit():
    return f"The recursion limit is: {sys.getrecursionlimit()}"
if __name__ == "__main__":
    print(recursion_limit())