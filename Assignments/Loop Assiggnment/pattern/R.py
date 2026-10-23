
# *****
# *   *
# *   *
# *****
# **   
# * *  
# *  * 
for i in range(1, 8):
    for j in range(1, 6):

        if j == 1:
            print('*', end='')

        elif i == 1 or i == 4:
            print('*', end='')

        elif j == 5 and i < 4:
            print('*', end='')

        elif i > 4 and j == i - 3:
            print('*', end='')

        else:
            print(' ', end='')

    print()