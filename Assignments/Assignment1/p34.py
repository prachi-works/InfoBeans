# 34. A wooded area is in the shape of a a trapezoid whose bases measure 128 m and 92 m and its height is 40 m. A 4 m wide walkway is constructed which runs perpendicular to the two bases. Calculate the area of the wooded area after the addition of the walkway.

base_1= 128
base_2=92
height = 40 
path_width = 4

total_trapeziod_area = ((base_1+base_2)/2) * height
path_area= path_width * height
final_wooded_area = total_trapeziod_area- path_area

#sliding the piece together
final_wooded_area_2 = (((base_1 - path_width) + (base_2 - path_width)) / 2) * height

print(f"Total Initial area is :{int(total_trapeziod_area)}")
print(f"walkaway area is :{path_area}")
print(f"Final Wooden Area:{int(final_wooded_area)}")