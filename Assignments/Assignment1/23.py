# 23. Find the number of cubical boxes of cubical side 3 cm which can be accommodated in carton of dimensions 15 cm × 9 cm × 12 cm.

cubical_side = 3
volume_of_cubicalboxes= cubical_side ** 3
print(f"Volume of cubicalboxes are {volume_of_cubicalboxes}")

length_of_carton=15
breadth_of_carton=9
height_of_carton=12
volume_of_carton = length_of_carton * breadth_of_carton *height_of_carton
print(f"Volume of carton {volume_of_carton}")

no_of_cubical_boxes= volume_of_carton / volume_of_cubicalboxes

print(f"Number of cubical boxes accomodated with {no_of_cubical_boxes:.0f}")