
# ***** *****
# ****  ****
# ***    ***
# **      **
# *        *
for i in range(5,0,-1):
    for j in range(i):
        print('*',end='')

    for _ in range(2*(6-i)-1):
        print(" ",end='')

    for j in range(i):
        print('*',end='')
    print()