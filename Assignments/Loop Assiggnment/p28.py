#    25) 1	27	125	343	…………
n=int(input('enter the no:'))
for i in range(1,n+1):
    if(i%2 != 0):
        print(i*i*i,end=' ')
    i+=1