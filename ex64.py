from ex63 import abs_path
import os
import time
#  Write a Python program that retrieves the date and time of file creation and modification.
def date_time_created_modified(p):
    c = os.path.getctime(p)
    m = os.path.getmtime(p)
    time_c = time.ctime(c)
    time_m = time.ctime(m)

    return f"The file was created at {time_c} and was last modified at {time_m}"
if __name__ == "__main__":
    path = abs_path("test.txt")
    print(date_time_created_modified(path))