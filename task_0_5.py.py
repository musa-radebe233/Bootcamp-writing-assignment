# Task 0.5
def area(a, b, c,):
    a = int(3)
    b = int(4)
    c = int(5)
    s_perimeter = 1/2 * (a + b + c)
    area = (s_perimeter * ((s_perimeter - a)*(s_perimeter - b)*(s_perimeter - c))) **0.5
    return area
print(area(3, 4, 5,))
    

