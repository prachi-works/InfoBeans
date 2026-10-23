for i in range(1,8):
    for j in range(1,6):
        if i==1 or i==4 or j==1:
            print('*',end='')
        elif i<=4 and j==5:
            print('*',end='')
        else:
            print(" ",end='')
    print()