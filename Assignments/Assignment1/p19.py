# 19. A cube with an edge of 7 cm and a cuboid measuring 7 cm × 4 cm × 8 am are kept on a table. Which shape has more volume?

side_of_cube = 7

volume_of_cube = side_of_cube ** 3

print(f"volume of cube is :{volume_of_cube}")

length_of_cuboid= 7
breadth_of_cuboid=4
height_of_cuboid = 8 

volume_of_cuboid= length_of_cuboid * breadth_of_cuboid * height_of_cuboid

print(f"Volume of cuboid is {volume_of_cuboid}")

difference = volume_of_cube - volume_of_cuboid

if volume_of_cube > volume_of_cuboid:
    print(f"The Cube volume is more by {difference} cm3")

elif volume_of_cuboid> volume_of_cube:
    print(f"The Cuboid volume is more by {difference} cm3")

else:
    print("Both shape have the exact same volume")