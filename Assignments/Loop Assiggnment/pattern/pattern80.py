# A B C D E
#   A B C D
#     A B C
#       A B
#         A 

for i in range(6,0,-1):
    for _ in range(6-i):
        print(" ",end=' ')
    for j in range(1,i):
        print(chr(64+j),end=' ')
    print()