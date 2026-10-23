# ABCDE
# A__D
# A_C
# AB
# A

for i in range(1,6):
    for space in range(i-1):
        print(' ',end='')
    for j in range(1,6-i+1):
        if i==1:
            print(chr(64+j),end='')
        elif j==1 or j==6-i:
            print(chr(64+j),end='')
        else:
            print('-',end='')
    print()