# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 

for i in range(5,0,-1):
    for _ in range(5-i):
        print(" ",end=' ')
    for j in range(i):
        print("*",end=' ')
    print()