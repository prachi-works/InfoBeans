# 3. How many tiles whose length and breadth are 13 cm and 7 cm respectively are needed to cover a rectangular region whose length and breadth are 520 cm and 140 cm? 

length=13
breadth=7

length1=520
breadth1=140

area_of_one_tiles= length * breadth

print("Area of one tiles is ",area_of_one_tiles)

area_of_rectangular_region= length1 * breadth1

print("Area of Rectangular Region is ",area_of_rectangular_region)

no_of_tiles= area_of_rectangular_region / area_of_one_tiles

print(f"Total no of tiles are {no_of_tiles}")