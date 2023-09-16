# Write a Python program to find the available built-in modules.
def built_in():
    return help("modules")

if __name__ == "__main__":
    print(built_in())