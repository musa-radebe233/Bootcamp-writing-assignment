# Task 0.10
var1 = input("Enter any word:")
var2 = input("Enter second word:")
letters = list(set(var1)&set(var2))
print("Common letters:")
for i in letters:
    print(i)
