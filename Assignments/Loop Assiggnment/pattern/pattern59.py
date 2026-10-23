# 12345
# 1__4
# 1_3
# 12
# 1
for i in range(1,6):
    for _ in range(i):
        print(' ',end='')
    for  j in range(1,6):
        if i==1:
            print(j,end='')
        elif j<=6-i:
            if j==1 or j==6-i:
                print(j,end='')
            else:
                print('-',end='')
    print()