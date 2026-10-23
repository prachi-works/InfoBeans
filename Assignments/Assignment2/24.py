# 24. How many bricks each 25 cm long, 10 cm wide and 7.5 cm thick will be required for a wall 20 m long, 2 m high and 0.75 m thick? If bricks sell at $900 per thousand what will it cost to build the wall?

# Brick dimensions (in cm)
brick_length = 25
brick_width = 10
brick_thickness = 7.5

# Wall dimensions (given in meters, converted to cm since 1m = 100cm)
wall_length = 20 * 100
wall_height = 2 * 100
wall_thickness = 0.75 * 100

# Cost parameters
price_per_thousand_bricks = 900

#  Calculate Volume of 1 Brick
brick_volume = brick_length * brick_width * brick_thickness

#  Calculate Volume of the Wall
wall_volume = wall_length * wall_height * wall_thickness

#  Calculate the number of bricks required
number_of_bricks = wall_volume / brick_volume

#  Calculate the total cost to build the wall
total_cost = (number_of_bricks / 1000) * price_per_thousand_bricks

# Print the results
print(f"Number of bricks required: {number_of_bricks:.0f}")
print(f"Total cost to build the wall: ${total_cost:.2f}")
