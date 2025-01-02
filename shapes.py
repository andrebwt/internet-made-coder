import math

# Calculate the area of a rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length*breadth
print(f"The area of the rectangle with length {length} and breadth {breadth} is: {area}")

# Calculate the area of a circle
radius = float(input("\nEnter the radius of the circle: "))
area = math.pi*math.pow(radius, 2)
print(f"The area of the circle with radius {radius} is: {area:.2f}")

# Calculate the area of a triangle
base = float(input("\nEnter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle with base {base} and height {height} is: {area:.2f}")
