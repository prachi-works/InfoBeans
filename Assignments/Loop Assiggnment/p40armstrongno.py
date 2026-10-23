# 38) WAP to check whether entered number is Armstrong or not

n=int(input('enter the no.'))
temp=n
length=0
while(n!=0):
    length+=1
    n=n//10

n=temp
sum=0
while(n!=0):
    r=n%10
    sum=sum+r**length
    n=n//10
    
if(sum==temp):
    print('armstrong no.')
else:
    print('not armstrong no.')