# 8. Write a Python program to display the first and last colors from the following list.

def colors(l):
    return l[0], l[-1]

if __name__ == "__main__":
    color_list = ["Red","Green","White" ,"Black"]
    print(colors(color_list))