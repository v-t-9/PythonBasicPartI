import os
# Write a Python program to divide a path by the extension separator.

if __name__ == "__main__":
    path = "PythonBasicPartI\ex106.py"
    print(os.path.split(path)[0], os.path.splitext(os.path.split(path)[1])[0], os.path.splitext(os.path.split(path)[1])[1])
   