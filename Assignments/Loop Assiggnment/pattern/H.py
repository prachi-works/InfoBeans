# *     * 
# *     * 
# *     * 
# * * * * 
# *     * 
# *     * 
# *     * 
for i in range(1,8):
    for j in range(1,5):
        if i==4 or j==1 or j==4:
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()