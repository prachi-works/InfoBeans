# *     *
# **    *
# * *   *
# *  *  *
# *   * *
# *    **
# *     *
for i in range(1,8):
    for j in range(1,8):
        if j==1 or j==7 or j==i:
            print('*',end='')
        else:
            print(' ',end='')
    print()