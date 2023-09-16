# Write a Python program to calculate the midpoints of a line.
def midpoints(x1,x2,y1,y2):
    return (((x1+x2)/2),((y1+y2)/2))


if __name__ == "__main__":
    x1 = float(input("First x endpoint: "))
    y1 = float(input("First y endpoint: "))
    x2 = float(input("Second x endpoint: "))
    y2 = float(input("Second y endpoint: "))
    print(midpoints(x1,x2,y1,y2))
