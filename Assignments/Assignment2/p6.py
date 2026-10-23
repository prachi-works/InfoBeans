# 6.Find the area of a triangle, sides of which are 10 cm and 9 cm and the perimeter 36 cm.

side_a=10
side_b=9
perimeter=36

side_c = perimeter - ( side_a + side_b)

#we have to find the semiperimeter
s= perimeter / 2

#Area of triangle is by herons formula 
area = ((s * ( s-side_a)*(s-side_b)*(s-side_c))** 0.5)
print(f"Area of triangle is {area} ")

