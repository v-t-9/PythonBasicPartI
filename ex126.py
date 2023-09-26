import inspect
from datetime import time
# Write a Python program to get the actual module object for a given object.

if __name__ == "__main__":
    print(inspect.getmodule(time))

