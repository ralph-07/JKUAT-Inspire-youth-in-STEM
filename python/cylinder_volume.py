# Formula to get volume of a cylinder
# V =
import math
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))
print(cylinder_volume(radius, height))

import math
def triangle_area(base, height):
    return 0.5 * base * height

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
print(triangle_area(base, height))

import math
def rectangle_area(length, width):
    return length * width
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
print(rectangle_area(length, width))