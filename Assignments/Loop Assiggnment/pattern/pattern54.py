1
11
1*1
1**1
11111

for i in range(1, 6):
    for space in range(5 - i):
        print(" ", end='')

    for j in range(i):
        if i == 3 and j == 1:
            print('*', end='')
        elif i == 4 and (j == 1 or j == 2):
            print('*', end='')
        else:
            print('1', end='')

    print()