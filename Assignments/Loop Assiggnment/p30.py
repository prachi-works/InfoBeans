# 20) 0	7	14	21	28	35	....
n=int(input('enter the no'))
for i in range(n+1):
    if(i%7 == 0):
        print(i,end=' ')
    i+=1
