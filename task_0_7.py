def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit
print("fahrenheit:", celsius_to_fahrenheit(40))

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    return celsius 
print("celsius:", fahrenheit_to_celsius(100))
