# 34) WAP to check whether entered number is perfect or not
#perfect no. is that whose sum of their factor = that number

n=int(input('enter the no.'))
i=1
sum=0

for i in range(1,n//2+1):
    if(n%i == 0):
        sum=sum+i
if(sum==n):
    print('perfect no')
else:
    print('not perfect no')
