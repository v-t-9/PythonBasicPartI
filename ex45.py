import os
# Write a Python program that calls an external command.

external_command = lambda c: os.system(c)
if __name__ == "__main__":
    c = "dir /ON"
    print(external_command(c))