# 18. Ron jogs around a rectangular park of length 50 m and breadth 30 m. If he takes 10 rounds of the park each day, how much distance does he cover in a day in km?

#Given
length = 50   #in meter 
breadth = 30  #in meter
round = 10

#Calculate the distance of 1 round (perimeter of the rectangle )
perimeter = 2 * ( length + breadth)

#calculate distance for 10 rounds in m
total_distance_meters =  perimeter * round

#cacluclate total distance in km
total_distance_kms= total_distance_meters / 1000

#print the result 
print(f"The total distance covered in a day :{total_distance_kms} km")





