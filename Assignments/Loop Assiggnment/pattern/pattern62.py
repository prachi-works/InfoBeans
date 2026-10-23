# ABCDE
#  ABCD
#   ABC
#    AB
#     A

for i in range(1,6):
    for _ in range(i-1):
        print(" ",end='')
    for j in range(1,6-i+1):
        print(chr(64+j),end='')
    print()
