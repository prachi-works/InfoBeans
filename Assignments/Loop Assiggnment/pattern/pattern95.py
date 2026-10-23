# ***** *****
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# ***** *****

for i in range(1,11):
    if i<=5:
        n=6-i
    else:
        n=i-5

    for j in range(n):
        print("*",end='')

    for j in range(2*(6-n)-1):
        print(" ",end='')
    for j in range(n):
        print('*',end='')
    print()