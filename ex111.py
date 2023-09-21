from pathlib import Path
# Write a Python program to make file lists from the current directory using a wildcard.

if __name__ =="__main__":
    for path in Path("\OtrosRepos\PythonBasicPartI").glob("*.py"):
        print(path)