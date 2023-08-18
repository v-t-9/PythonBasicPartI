# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
future_value = lambda q,int,y: q*(1+(int/100))**y
if __name__ == "__main__":
    amt = 10000
    int = 3.5
    years = 7
    print(future_value(amt,int,years))