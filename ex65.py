# Write a Python program that converts seconds into days, hours, minutes, and seconds.
def time(s):
    if s>=86400:
        d = s/86400
        da = int(d)
        h = (d-da)*24
        hr = int(h)
        m = (h-hr)*60
        mi = int(m)
        sec = int((m-mi)*60)
    else:
        d = 0
        h = s/3600
        hr = int(h)
        m = (h-hr)*60
        mi = int(m)
        sec = (m-mi)*60
        
    return f"The seconds are equivalento to {da} days, {hr} hours, {mi} minutes and {sec} seconds"
if __name__ == "__main__":
    sec = int(input("Enter seconds: "))
    print(time(sec))
