import os
import glob
# Write a Python program to sort files by date.

def files_by_date(p):
    files = glob.glob(p)
    files.sort(key=os.path.getmtime)
    return files
if __name__ == "__main__":
    
    print(files_by_date("*.txt"))