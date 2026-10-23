#    1    4-1
#   12    4-2
#  123    4-3
# 1234
#  123
#   12
#    1
for i in range(1,8):
    if i<=4:
        n=i
    else:
        n = 8 - i
    for space in range(4-n):
        print(" ",end='')
    for j in range(1,n+1):
        print(j,end='')
    print()