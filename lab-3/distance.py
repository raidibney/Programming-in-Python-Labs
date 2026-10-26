

import math


x1 = float(input("Enter the x1 coordinate: "))
y1 = float(input("Enter the y1 coordinate: "))
x2 = float(input("Enter the x2 coordinate: "))
y2 = float(input("Enter the y2 coordinate: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The distance between the two points is: " + str(distance))