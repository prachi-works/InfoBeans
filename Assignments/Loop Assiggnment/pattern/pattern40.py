# 55555
# 4  4
# 3 3
# 22
# 1

for i in range(5,0,-1):
    if i == 5:
        print(str(i) * i)
    elif i == 1:
        print(i)
    else:
        print(str(i) + " " * (i - 2) + str(i))
  
    
