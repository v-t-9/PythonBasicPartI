# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

def filename_extension(filename):
    f = filename.split(".")
    return f"The extension of the file is {f[1]}"

if __name__ == "__main__":
    inp = input("Name of your file: ")
    print(filename_extension(inp))