# *     *
# **   **
# * * * *
# *  *  *
# *     *
# *     *
# *     *
for i in range(1, 8):
    for j in range(1, 8):
        if j == 1 or j == 7:
            print('*', end='')
        elif i <= 4 and (j == i or j == 8-i):
            print('*', end='')
        else:
            print(' ', end='')
    print()