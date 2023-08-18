import os
# Write a Python program to find out the number of CPUs used.

def num_cpus():
    return os.cpu_count()
if __name__ == "__main__":
    print(num_cpus())