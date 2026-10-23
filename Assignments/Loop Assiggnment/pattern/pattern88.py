# *
# *_*
# *_*_*
# *_*_*_*
# *_*_*
# *_*
# *  

for i in range(1,8):
    if i<=4:
        n=i
    else:
        n=8-i
    for j in range(n):
        if j==n-1:    #n=3(1,2) and j==2 if 2==2 print * other wise *_
            print('*',end='')
        else:
            print("*_",end='')
    print()