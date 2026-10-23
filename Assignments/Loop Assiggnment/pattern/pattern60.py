for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end='')
    for j in range(1,i+1):
        if i==5:
            print(i,end='')
        elif j==1 or j==i:
            print(i,end='')
        else:
            print('-',end='')
    print()