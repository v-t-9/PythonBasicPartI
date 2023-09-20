import os
# Write a Python program to get the effective group id,  effective user id, real group id, and a list of supplemental group ids associated with the current process.

if __name__ == "__main__":
    print("Group id", os.getpgrp())
    print("Process id:",os.getpid())
    print("Process' real, effective, and saved group ids",os.getresgid())
    print("List of supplementary group ids associated with the current process",os.getgroups())
    