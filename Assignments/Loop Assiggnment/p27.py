#  0	4	16	36	64	….. 1 2 3 4 5 6 7 8

n=int(input('enter the number:'))
for i in range(n+1):
    if(i%2 == 0):
        print(i*i,end=' ')
    i+=1
    