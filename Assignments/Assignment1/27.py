#  27. Find the cost of tiling a dining room 20 m long and 15 m wide at the rate of $ 5 per square m
length = 20
breadth = 15 
rate_per_square=5

#area of dining room
area= length * breadth

#cost of tiling a dining room
cost_tile = area * rate_per_square

print(f"Area of dining room is {area} m2")
print(f"Total cost of tiling : ${cost_tile:.2f}")
