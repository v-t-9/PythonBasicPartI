import os
# Write a Python program to find files and skip directories in a given directory.

def find_files(p,f):
    r = []
    for i in os.listdir(p):
        if os.path.isfile(i):
            r.append(i)
    return r
if __name__ == "__main__":
    path = "\OtrosRepos\PythonBasicPartI"
    file = "test.txt"
    print(find_files(path, file))