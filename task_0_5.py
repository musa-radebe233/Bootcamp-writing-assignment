def area(length1, length2, length3):
    semi_perimeter = 1/2 * (length1 + length2 + length3)
    area = (semi_perimeter * ((semi_perimeter - length1)*(semi_perimeter - length2)*(semi_perimeter -length3))) **0.5
    return area
print(area(3, 4, 5))
    

