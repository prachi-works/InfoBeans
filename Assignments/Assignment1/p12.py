# 12. Find the area of a right angled triangle whose hypotenuse is 13 cm and one of its sides containing the right angle is 12 cm. Find the length of the other side.
import math
hyptoneous = 13
side_1 = 12 

#hypotoneous^2 = side_1  ^ 2 + side_2 ^2
side_2 = math.sqrt((hyptoneous ** 2 ) - (side_1 ** 2))

# Step 2: Calculate Area (0.5 * base * height)
# In a right-angled triangle, the two shorter sides are the base and height
area = 0.5 * side_1 * side_2

print(f"length of other side:{side_2} cm") #output :  5.0
print(f"Area of triangle is :{area:.0f} cm2") #.0f removes the  decimal value .0 and show int value
