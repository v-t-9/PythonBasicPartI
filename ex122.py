# Write a Python program to empty a variable without destroying it.
empty_variable = lambda v: type(v)()

if __name__ == "__main__":
    n=20
    d = {"x":200}
    l = [1, 2, 3]
    t = (1, 2, 3)
    s = {1, 2, 3}
    print(empty_variable(n))
    print(empty_variable(d))
    print(empty_variable(l))
    print(empty_variable(t))
    print(empty_variable(s))