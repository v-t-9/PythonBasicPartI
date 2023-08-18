import sys
# Write a Python program to locate Python site packages.

def site_packages():
    # i represent the directories
    for i in sys.path:
        if i.endswith("site-packages"):
            return i
if __name__ == "__main__":
    print(site_packages())