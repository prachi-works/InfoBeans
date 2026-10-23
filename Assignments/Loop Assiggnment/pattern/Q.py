# *******
# *     *
# *     *
# *     *
# *   * *
# *    * 
# ***** *
for i in range(1, 8):
    for j in range(1, 8):
        if i == 1 or j == 1 or (i == 7 and j <= 5):
            print('*', end='')
        elif j == 7 and i <= 5:
            print('*', end='')
        elif i >= 5 and j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()