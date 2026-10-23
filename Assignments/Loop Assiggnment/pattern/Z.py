# *********
#       *  
#      *   
#     *    
#    *     
#   *      
#  *       
# *        
# *********
for i in range(1,10):
    for j in range(1,10):
        if i==1 or i==9 or j==9-i:
            print('*',end='')
        else:
            print(' ',end='')
    print()
                 