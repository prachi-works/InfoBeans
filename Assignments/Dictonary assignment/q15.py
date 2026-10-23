# 15. Create a dictionary in which numbers from 1 to 5 are keys and their
#     squares are values.
l=[1,2,3,4,5]
result={element:element * element for element in l}
print(result)      #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}