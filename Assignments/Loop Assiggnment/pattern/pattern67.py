
#       X 
#      X X 
#     X - X 
#    X - - X 
#   X X X X X 

for i in range(1,6):
    print(" "*(6-i),end=' ')
    for j in range(1,i+1):
        if i==1 or i==5 or (j==1 or j==i):
            print("X",end=' ')
        else:
            print("-",end=' ')
    print()
           
