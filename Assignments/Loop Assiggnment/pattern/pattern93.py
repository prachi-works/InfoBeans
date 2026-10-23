# *        *
# **      **
# ***    ***
# ****  ****
# ***** *****
for i in range(1,6):

    #left stars
    for j in range(i):
        print('*',end='')

    #spaces
    for _ in range(2 * (5-i)+1):      #if (5-i)-1 then no space in between two groups
        print(" ",end='')

    #right stars 
    for j in range(i):
        print('*',end='')
    print()