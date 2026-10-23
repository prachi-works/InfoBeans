# *     *
#  *   * 
#   * *  
#    *   
#    *   
#    *   
#    *   
for i in range(1,8):
    for j in range(1,8):
        if i<=4 and (j==i or j==8-i):
            print('*',end='')
        elif i>4 and j==4:
            print('*',end='')
        else:
            print(' ',end='')
    print()