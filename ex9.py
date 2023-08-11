from datetime import datetime
#  Write a Python program to display the examination schedule. (extract the date from exam_st_date).
#   exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

def examination_schedule(d):
    ye,mo, da = d[::-1]
    date = datetime(ye, mo, da)
    return f"Exam starts: {date.day}/{date.month}/{date.year}"

if __name__=="__main__":
    exam_st_date = (11, 12, 2014)
    print(examination_schedule(exam_st_date))