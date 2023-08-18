# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2)


distance = lambda x1,x2,y1,y2: (abs(x2-x1)**2 + abs(y2-y1**2))**(1/2)
if __name__ == "__main__":
    x1 = 4
    x2 = 0
    y1 = 6
    y2 = 6
    print(distance(x1,x2,y1,y2))