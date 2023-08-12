
from datetime import datetime
# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

def calculate_days(d1, d2):
    ye,mo, da = d1
    date1 = datetime(ye, mo, da)
    ye,mo, da = d2
    date2 = datetime(ye,mo, da)

    res = date1 - date2
    return f"{abs(res.days)} days"

if __name__ == "__main__":
    d1 = (2014, 7, 2)
    d2 = (2014, 7, 11)

    print(calculate_days(d1, d2))