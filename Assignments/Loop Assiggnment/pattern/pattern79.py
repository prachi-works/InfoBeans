# 123456789
#  1234567
#   12345
#    123
#     1

for i in range(5,0,-1):
    for _ in range(5-i):
        print(" ",end='')
    for j in range(1,2*i):
        print(j,end='')
    print()