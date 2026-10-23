
for i in range(1,10):
    if i<=5:
        n=i
    else:
        n=10-i

    #spaces
    for space in range(5-n):
        print(" ",end='')

    #binary pattern
    for j in range(n*2-1):
        if j%2 == 0:
            print('1',end='')
        else:
            print('0',end='')
    print()