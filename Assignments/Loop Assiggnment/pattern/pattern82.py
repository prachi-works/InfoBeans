# 123456789
#  1     7
#   1   5
#    1 3
#     1

for i in range(5,0,-1):
    for _ in range(5-i):
        print(" ",end='')
    for j in range(1,2*i):
        if i==5:
            print(j,end='')
        elif j==1 or j==2*i-1:
            print(j,end='')
        else:
            print(" ",end='')
    print()