# *
# ***
# ***** 
# ******* 
# ***** 
# *** 
# *

for i in range(1,8):
    if i<=4:
        n=i
    else:
        n=8-i
    for space in range(4-n):
        print(" ",end='')
    
    for j in range(2*n-1):
        print("*",end='')
    print()