import os
# Write a Python program to extract the filename from a given path
def extract_filename(path):
    name = os.path.basename(path)
    return os.path.splitext(name)[0]
if __name__ == "__main__":
    path = "\PythonBasicPartI\ex103.py"
    print(extract_filename(path))