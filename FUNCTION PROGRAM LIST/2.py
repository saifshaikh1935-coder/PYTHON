import math

def rectangle(width, length):
    return width * length

def triangle(height, base):
    return 0.5 * height * base

def circle(radius):
    return math.pi * radius * radius

width = float(input("Enter rectangle width: "))
length = float(input("Enter rectangle length: "))
height = float(input("Enter triangle height: "))
base = float(input("Enter triangle base: "))
radius = float(input("Enter circle radius: "))

print("Area of rectangle =", rectangle(width, length))
print("Area of triangle =", triangle(height, base))
print("Area of circle =", circle(radius))
