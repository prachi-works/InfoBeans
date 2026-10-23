# 5 5 5 5 5 
#   4 4 4 4 
#     3 3 3 
#       2 2 
#         1 

for i in range(5,0,-1):
    for _ in range(5-i):
        print(" ",end=' ')
    for j in range(i):
        print(i,end=' ')
    print()
