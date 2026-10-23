# x
# xx
# xxx
# xxxx
# xxx
# xx
# x

for i in range(1,8):
    if i <= 4:
        n=i
    else:
        n=8-i  #after execution i will be 5
    for j in range(n):
        print('x',end='')
    print()

    