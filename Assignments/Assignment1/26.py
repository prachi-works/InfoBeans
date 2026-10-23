# 26. How many bricks will be required to lay a path 120 m long and 2.4 m breadth if a brick is 24 cm long and 15 cm wide?
path_length = 120 * 100
path_breadth = 2.4 * 100

path_area= path_length * path_breadth
print("the path area is ",path_area)

brick_length = 24 
brick_width= 15
brick_area= brick_length * brick_width
print("the brick area is ",brick_area)

no_of_bricks= path_area / brick_area
print("no of bricks requireds  are ",no_of_bricks)