# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49
solve = lambda x,y: (x + y) * (x + y)
if __name__ == "__main__":
    x = 4
    y = 3
    print(solve(x,y))