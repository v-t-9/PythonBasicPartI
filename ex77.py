import sys
# Write a Python program to test whether the system is a big-endian platform or a little-endian platform.
def endian_platform():
    if sys.byteorder == "big":
        return f"Big endian platform"
    if sys.byteorder == "little":
        return f"Little endian platform"
if __name__ == "__main__":
    print(endian_platform())