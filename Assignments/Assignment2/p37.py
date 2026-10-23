# 37. The surface of the cylinder is 149 cm². The cylinder height is 6 cm. What is the diameter of this cylinder?

cylinder_surface_area = 149 
cylinder_height= 6

#approximate  value for pi
pi= 3.14159

#surface_area= 2*pi*r(r+h)
# Setting up standard quadratic form components: a*r² + b*r + c = 0
# Formula: 2*pi*r² + 2*pi*r*h - Area = 0
a = 2 * pi
b = 2 * pi * cylinder_height
c= -cylinder_surface_area

# Using the Quadratic Formula: r = (-b + (b² - 4ac)^0.5) / 2a
discriminant = (b*b) - (4*a*c)
radius = (-b + (discriminant ** 0.5)) / (2 * a)

#diameter 
diameter = 2 * radius

print(f"Calculated Radius: {radius:.2f} cm")
print(f"Calculated Diameter: {diameter:.2f} cm")
