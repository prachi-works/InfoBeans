# 60) WAP to print Square, Cube and Square Root of all numbers from 1 to N
import math
n=int(input('enter the value of N:'))

for i in range(1,n+1):
    square= i ** 2
    cube = i ** 3
    square_root=math.sqrt(i)

    print("Number:",i)
    print('Square:',square)
    print('Cube:',cube)
    print('Square root:',square_root)
    print()