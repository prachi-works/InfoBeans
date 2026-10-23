# A
# B B
# C  C
# D    D
# EEEEEEEEE

for i in range(1,6):
    for _ in range(5-i):
        print(" ",end='')
    for j in range(1,2*i):
        if i==5:
            print('E',end='')
        elif j==1 or j==2*i-1:
             print(chr(64+i),end='')
        else:
            print(" ",end='')
    print()
