import math

def calculate_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

try:
    r = float(input("Enter the radius: "))
    area = calculate_area(r)
    print(f"The area of the circle is: {area}")
except ValueError as e:
    print(e)