# 29. How many square tiles of side 10 cm will be required to tile a floor measuring 800 cm by 900 cm?
# Floor dimensions (in cm)
floor_length = 800
floor_width = 900

# Square tile dimension (in cm)
tile_side = 10

# Step 1: Calculate the area of the floor
floor_area = floor_length * floor_width

# Step 2: Calculate the area of one square tile
tile_area = tile_side * tile_side

# Step 3: Calculate the number of tiles required
tiles_required = floor_area / tile_area

# Print the results
print(f"Area of the floor: {floor_area} cm²")
print(f"Area of one tile: {tile_area} cm²")
print(f"Number of square tiles required: {tiles_required:.0f}")
