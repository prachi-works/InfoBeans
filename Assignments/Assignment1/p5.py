# 5. If it costs 1600 rs. to fence a rectangular park of length 20 m at the rate of 25 rs. per m², find the breadth of the park and its perimeter. Also, find the area of the field.

total_cost = 1600
length = 20
rate = 25

perimeter = total_cost / rate 

print(f"The perimeter is {perimeter}")

# perimeter = 2 * ( length + breadth)

breadth = (perimeter / 2 ) - length
print(f"The breadth is {breadth}")

area_of_field= length * breadth
print(f"Area of field is {area_of_field}")
