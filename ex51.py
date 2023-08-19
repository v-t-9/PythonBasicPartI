import profile
# Write a Python program to determine the profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

def str_print(s):
    return s
if __name__ == "__main__":
    s = "Hello, how are you?"*20
    print(str_print(s))
    print(profile.run("str_print(s)"))