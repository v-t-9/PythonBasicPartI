#  Write a Python program to count the number of occurrences of a specific character in a string.
def num_ocurrences(s, c):
    count = 0
    for i in s:
        if c == i:
            count = count + 1
    return f"The character {c} appears {count} times in {s}"

if __name__ == "__main__":
    s = "hello, how are you?"
    c = "e"
    print(num_ocurrences(s,c))