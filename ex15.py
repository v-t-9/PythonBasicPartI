import math
# 15. Write a Python program to get the volume of a sphere with radius six.

volume_sphere = lambda r: (4/3)*(math.pi)*(r**3)

if __name__ == "__main__":
    rad = 6
    print(volume_sphere(rad))