# *       * 
# *     *   
# *   *     
# * *       
# *   *     
# *     *   
# *       * 
for i in range(1,8):
    for j in range(1,6):
        if j==1:
            print('*',end=' ')
        elif i<=4 and j==6-i:                        
            print('*',end=' ')
        elif i>=4 and j==i-2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()