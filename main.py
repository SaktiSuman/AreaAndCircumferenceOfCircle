import math
r = int(input("Enter the radius of the circle: "))
c = round(2 * math.pi * r, 2)
a = round(math.pi * r * r, 2)
print("Circumference: ",c)
print("Area: ",a)