# 28) 1	2	3	4	 Hello	6	7	8	9	Hello	11	12 …

n=int(input('enter the no.'))

for i in range(1,n+1):
    if(i!=0 and i%5 !=0):
        print(i,end=' ')
        i+=1
    else:
        print('Hello',end=' ')
