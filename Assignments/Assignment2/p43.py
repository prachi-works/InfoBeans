# 43. Find the cost of polishing the base of a cone whose height is 4cm and slant height 5 cm at the rate of 10 rs. Per sq. cm

height = 4.0        # in cm
slant_height = 5.0  # in cm
rate_per_sq_cm = 10 # in Rs.

# Approximate value for pi
pi = 3.14159

#  Find the radius (r) using Pythagoras theorem: slant_height² = radius² + height²
# Therefore, radius = (slant_height² - height²)^0.5
radius = ((slant_height * slant_height) - (height * height)) ** 0.5

#  Calculate the area of the circular base (Formula: pi * r²)
base_area = pi * (radius * radius)

# Calculate the total cost (Formula: area * rate)
total_cost = base_area * rate_per_sq_cm

print(f"Calculated Radius: {radius} cm")
print(f"Base Area: {base_area:.2f} cm2")
print(f"Total Cost of Polishing: Rs. {total_cost:.2f}")
