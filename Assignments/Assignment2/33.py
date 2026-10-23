# 33. A rectangular garden has dimensions of 30 m by 20 m and is divided in to 4 parts by two pathways that run perpendicular from its sides. One pathway has a width of 3 m and the other, 4 m. Calculate the total usable area of the garden.
#Dimensions of garden
garden_length=30
garden_width=20

#pathaway width 
path_a=3
path_b=4

#CAse1: 3 m cuts the length and 4 m cuts the width
usable_length = garden_length - path_a
usable_width= garden_width - path_b
area_case1= usable_length * usable_width

#CASE2: 4m cuts the length and 3m custs the width
usable_length1= garden_length - path_b
usable_width1= garden_width - path_a
area_case2 = usable_length1 * usable_width1

#usable area
print(f"Case 1 Usable Area: {area_case1} m2")
print(f"Case 2 Usable Area: {area_case2} m2")