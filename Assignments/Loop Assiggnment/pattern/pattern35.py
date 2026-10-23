# ABCDE
# ABCD
# ABC
# AB
# A

for i in range(6,0,-1):
    for j in range(1,i):
        print(chr(64+j),end='')
    print()