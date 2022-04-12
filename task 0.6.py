# Task 0.6
a = int(input("a is:"))
b = int(input("b is:"))
c = int(input("c is:"))

def highest(a, b, c):
    if b <= a >= c:
        return a
    elif a <= b >= c:
        return b
    elif a <= c >= b:
        return c
print(highest(a,b,c))
