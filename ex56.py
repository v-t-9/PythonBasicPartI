import os
# Write a Python program to get the height and width of the console window.

def width_height_console():
    return os.get_terminal_size()

if __name__ == "__main__":
    print(width_height_console())