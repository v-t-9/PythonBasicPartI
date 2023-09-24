# Write a Python program to prove that two string variables of the same value point to the same memory location.
memory_location = lambda s1,s2: s1 is s2
if __name__ == "__main__":
    s1 = "Hello"
    s2 = "Hello"
    s3 = "hello"
    print(memory_location(s1,s2))
    print(memory_location(s1,s3))