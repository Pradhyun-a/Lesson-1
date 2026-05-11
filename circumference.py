def circumference(radius):
    pi = 3.14159
    result = 2 * pi * radius
    return result

radius = float(input("Enter the radius of the circle: "))
c = circumference(radius)
print("The circumference of the circle is:", c)
