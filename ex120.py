# Write a Python program to format a specified string and limit the length of a string.

def limit_str(s):
    if len(s) >= 10:
        return s[:10]
    else:
        return s

if __name__ == "__main__":
    s = "Helloooooooooooooooooooooooooooooooooooooooooooooo"
    print(limit_str(s))


    
    
