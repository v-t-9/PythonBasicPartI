import os
import time
# Write a Python program to get a directory listing, sorted by creation date.
def dir_listing_by_creation_date(p):

    dir = os.listdir(p)
    ds = sorted(dir, key=os.path.getctime)
    t = [os.path.getctime(i) for i in dir]
    ts = sorted(t)
    t_dir = [time.ctime(i) for i in ts]
    z= list(zip(ds, t_dir))
    return z
        
    
  

if __name__ == "__main__":
    path = os.getcwd()
    print(dir_listing_by_creation_date(path))
