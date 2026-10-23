# * * * * * * * 
#             * 
#             * 
#             * 
#             * 
#   *         * 
for i in range(1,8):
    for j in range(1,8):
        if i==1 or j==7:
            print('*',end=' ')
        elif i==7 and j<=5 :
            print('*',end=' ')
        elif i==6 and j==2:
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()