# 15. Shelly has a rectangular garden of length 22 m and breath 15 m. Her friend Rachel has a square garden of side 21 m. Whose garden is bigger and by how much?

shelly_length = 22
shelly_width= 15
shelly_area= shelly_length * shelly_width

print(f"Shelly gardens area are {shelly_area}")

#Rachel's Square Garden
rachel_side= 21 
rachel_area = rachel_side ** 2
print(f"Racheal square garden area are{rachel_area}")

difference = abs(shelly_area-rachel_area)

#Print whose garden is bigger and how much
if shelly_area>rachel_area:
    print(f"shelly garder is bigger by {difference} m2")
elif rachel_area>shelly_area:
    print(f"rachel square garden is bigger {difference} m2")
else:
    print("Both garden have same area")