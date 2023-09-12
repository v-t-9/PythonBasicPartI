# Write a Python program to convert all units of time into seconds.

def seconds(t):
   t1 = t.split(" ")
   ti = [int(i) for i in t1]
   if ti[0]>365 or ti[1]>24 or ti[2]>60 or ti[3]>60:
        raise Exception("Try again")
   else:
        sd = ti[0] *3600 *24
        sh = ti[1]*3600
        sm = ti[2]*60
        s = ti[3]
        sec = sd + sh +sm + s

        return f"The time entered has {sec} seconds"

if __name__ == "__main__":
    time = input("Enter a time (d h m s) : ")
    print(seconds(time))