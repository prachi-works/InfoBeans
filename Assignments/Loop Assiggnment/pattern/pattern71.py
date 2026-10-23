#     *
#    *-*
#   *---*
#  *-----*
# *********

for i in range(1,6):
    for _ in range(5-i):
        print(" ",end='')
    for j in range(1,2*i):
        if i==1 or i==5 or j==1 or j==2*i-1:
            print('*',end='')
        else:
            print('-',end='')
    print()