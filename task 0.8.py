# Task 0.8
time = float(input("Time:"))
hours = int(time / 60)
x = float(time / 60)
minutes =(x - hours) * 60
print("%.2f hours %0.2f minutes" %(hours, minutes))
