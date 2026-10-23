# *       * 
# *       * 
# *       * 
# *       * 
# *       * 
# *       * 
# * * * * * 
for i in range(1,8):
    for j in range(1,6):
        if i==7 or j==1 or j==5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()