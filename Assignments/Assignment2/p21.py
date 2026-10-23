# 21. A brick measures 15 cm in length, 8 cm in breadth and 5 cm in height. How many bricks will be used to make a wall of length 15 m, breadth 10 m and height 8 metres?

brick_length=15
brick_breadth=8
brick_height=5

volume_of_brick= brick_breadth * brick_breadth * brick_height

wall_length = 15 * 100
wall_breadth = 10 * 100
wall_height = 8 * 100

volume_of_wall= wall_length * wall_breadth * wall_height

number_of_bricks = volume_of_wall / volume_of_brick

print(f"Volume of one brick:{volume_of_brick} cm3")
print(f"Volume of wall :{volume_of_wall} cm3")
print(f"Number of bricks required :{number_of_bricks:.0f}")