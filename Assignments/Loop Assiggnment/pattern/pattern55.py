# A
# AB
# A_C
# A__D
# ABCDE

for i in range(1,6):
    for _ in range(1,6-i):
        print(" ",end='')
    for  j in range(1,i+1):
        if(i==3 and j==2):
            print("-",end='')
        elif(i==4 and (j==2 or j==3)):
            print("-",end='')
        else:
            print(chr(64+j),end='')
    print()
    

