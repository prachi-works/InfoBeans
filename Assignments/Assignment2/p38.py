# 38. The cylinder has a volume of 1287. The base has a radius 10. What is the area of the surface of the cylinder?

#given
volume_cylinder=1287
radius = 10

#volume of cylinder = 3.14 * r ^2 *h
height = volume_cylinder/ 3.14 * radius *radius

#surface area of cylidner
total_area= 2 * 3.14 * radius * (radius + height)
print(f"The total surface of the cylinder is{total_area}")
