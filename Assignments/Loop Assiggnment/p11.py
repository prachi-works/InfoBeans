#  WAP to print N odd numbers.

N=int(input('enter the no.'))

number=1
count=0

while(count <= N):
    print(number , end=' ')
    number += 2
    count += 1