# Task 0.1
x = 0
y = 1
print(x)
print(y)
x = x + 3
y = y + x
print(x)
print(y)
# Task 0.2
x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + (1 * 2)
a = 1 + 1 * 2/2
b = (1 + 1 * 2)/2
things = [x, y, z, a, b]
print(all(things))
# Task 0.3
def hello(name):
    print(name + "!")
hello("Tshepo")
# Task 0.4
x = int(input("interger:"))
def even_or_odd(x):
    if (x % 2)== 0:
        return("even")
    else:
        return("odd")
print(even_or_odd(x))
# Task 0.5
b = float(input("b is:"))
h = float(input("h is:"))
x = 1/2

def area(x, b, h):
    triangle = 1/2 * b * h
    return triangle
print(area(x, b, h))
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
 
# Task 0.7
celsius = float(input("Temperature in celsius:"))
fahrenheit = (celsius * 9/5) + 32
print("%f fahrenheit" %(fahrenheit))

fahrenheit = float(input("Temperature in fahrenheit:"))
celsius = (fahrenheit - 32) * 5/9
print("%f celsius" %(celsius))
# Task 0.8
time = float(input("Time:"))
hours = int(time / 60)
x = float(time / 60)
minutes =(x - hours) * 60
print("%.2f hours %0.2f minutes" %(hours, minutes))
# Task 0.9
def vowel(text):
    vowels = "aeiou"
    i = [letter for letter in text.lower()if letter in vowels]
    print("Vowels:")
    print(i)
vowel (input("Enter any word:"))
# Task 0.10
var1 = input("Enter any word:")
var2 = input("Enter second word:")
letters = list(set(var1)&set(var2))
print("Common letters:")
for i in letters:
    print(i)





    
