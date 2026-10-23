# 25. 100 bricks of length 24 cm and breadth 15 cm are used to tile a path of a garden. What is the area of the path?

num_brick=100
brick_length=24
brick_breadth=15

#area of one brick 
brick_area = brick_length * brick_breadth

#total area of path in square centimeter sq 
path_area_cm2= brick_area * num_brick

# Step 3: Convert the total area to square meters (1 m² = 10,000 cm²)
path_area_m2 = path_area_cm2 / 10000

# Print the results
print(f"Area of the path: {path_area_cm2} cm²")
print(f"Area of the path: {path_area_m2:.2f} m²")