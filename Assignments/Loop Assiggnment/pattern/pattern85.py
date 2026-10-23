1
12
123
1234
123
12
1

for i in range(1,8):
    if i<=4:
        n=i
    else:
        n= 8 - i
    for j in range(1,n+1):
        print(j,end='')
    print()