# 4. Find the cost of tiling a rectangular plot of land 300 m long and 150 m wide at the rate of $6 per hundred square m. 
length=300
breadth=150

area = length * breadth 
print(f"area of rectangular plot is {area}")

# The tiling rate is given as $6 per \(100\text{ m}^2\). To find how many "\(100\text{ m}^2\) units" fit into the plot, divide the total area by 100:

number_of_hundred_sq_units= area / 100
print(number_of_hundred_sq_units)

total_cost = number_of_hundred_sq_units * 6

print(f"The total cost is {total_cost}")