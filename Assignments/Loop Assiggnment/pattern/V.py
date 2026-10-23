# *           *
#  *         * 
#   *       *  
#    *     *   
#     *   *    
#      * *     
#       *      
for i in range(1,8):
    for j in range(1,14):
        if j==i or j==14-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()