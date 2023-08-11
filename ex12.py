import calendar
#  Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

def cal_for_given_month_year(y,m):
    return calendar.month(y,m)

if __name__ == "__main__":
    print(cal_for_given_month_year(2023,8))