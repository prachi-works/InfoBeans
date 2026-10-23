# *
# *_* 
# *___* 
# *_____*
# *___* 
# *_*
# *

for i in range(1,8):
    if i<=4:
        n=i
    else:
        n=8-i
    for _ in range(4-n):
        print(" ",end='')
    for j in range(2*n-1):
        if j == 0 or j == 2 * n - 2:
            print("*", end='')
        else:
            print("_", end='')

    print()