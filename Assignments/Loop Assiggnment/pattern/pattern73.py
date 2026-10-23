#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1 
#  1 4 6 4 1 

for i in range(5):
    n=1
    for space in range(5-i):
        print(" ",end='')
    for j in range(i+1):
        print(n,end=' ')
        n = n * (i-j) //(j+1)
    print()