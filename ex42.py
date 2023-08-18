import struct
# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

def mode_32_or_64():
    return struct.calcsize("P")*8

if __name__ == "__main__":
    print(mode_32_or_64())