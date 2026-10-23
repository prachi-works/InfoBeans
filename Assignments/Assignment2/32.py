# 32. A square garden with a side length of 150 m has a square swimming pool in the very centre with a side length of 25 m . Calculate the area of the garden.

garden_side = 150
total_area = garden_side * garden_side
print(f"total area enclosed by the garden fence {total_area}")

pool_side=25
pool_area= pool_side * pool_side

#Remaining garden area
garden_area = total_area - pool_area

print(f"The total area of garden exluding the pool is {garden_area}")