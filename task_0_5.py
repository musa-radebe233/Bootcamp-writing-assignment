def area(a, b, c,):
    semi_perimeter = 1/2 * (a + b + c)
    area = (semi_perimeter * ((semi_perimeter - a)*(semi_perimeter - b)*(semi_perimeter - c))) **0.5
    return area
print(area(3, 4, 5,))
    

