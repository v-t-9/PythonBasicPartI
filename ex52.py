import sys
# Write a Python program to print to STDERR.
def print_to_STDERR():
    return f"Hello!!!"
if __name__ == "__main__":
    print(print_to_STDERR(), file=sys.stderr)