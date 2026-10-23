# 1
# 1 2
# 1  3
# 1   4
# 1  3
# 1 2
# 1

for i in range(1,8):
    if i<=4:
        n=i
    else:
        n = 8 - i
    for j in range(1,n+1):
        if j==1 or j==n:
            print(j,end='')
        else:
            print(' ',end='')
    print()