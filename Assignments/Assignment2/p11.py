
# 11. The base and height of a triangle are in the ratio 8 : 5 and its area is 320 m². Find the height and base of the triangle.

import math

#Given ratio
area = 320
base_ratio=8
height_ratio=5

# Calculate the common multiplier 'x'
x_squared = area / (0.5 * base_ratio * height_ratio)
x = math.sqrt(x_squared)

base = base_ratio * x      # 8 * 4.0 = 32.0
height = height_ratio * x  # 5 * 4.0 = 20.0

print(f"Base of the triangle: {base} meters")
print(f"Height of the triangle: {height} meters")

