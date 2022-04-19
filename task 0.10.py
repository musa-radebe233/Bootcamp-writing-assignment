# Task 0.10
def common_letters(var1, var2):
    letters = list(set(var1)&set(var2))
    print("Common letters:")
    for i in letters:
        print(",", ",".join(i), end = ' ')
common_letters("pie", "spice")



    
