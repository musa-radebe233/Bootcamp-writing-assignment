# Task 0.6
def highest(num1, num2, num3):
    if num2 <= num1 >= num3:
        return num1
    elif num1 <= num2 >= num3:
        return num2
    elif num1 <= num3 >= num2:
        return num3
print(highest(3,5,4))
