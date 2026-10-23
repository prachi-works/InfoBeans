# 30. How many tiles of length 5 cm and breadth 8 cm are needed to tile the floor of a bed room 200 cm long and 400 cm wide?
floor_length=200
floor_breadth=400

floor_area= floor_length * floor_breadth
print("Floor area is ",floor_area)


tile_length=5
tile_breadth=8

tile_area = tile_length * tile_breadth
print("Tile area  is ",tile_area)

no_of_tile = floor_area / tile_area
print("Number of tile we needed it are",no_of_tile)