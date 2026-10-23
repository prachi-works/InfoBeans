# 39) WAP to check whether entered number is strong or not
import math
n=int(input('enter the no.'))
temp=n
sum=0

while temp>0:
    r=temp%10
    sum += math.factorial(r)
    temp=temp//10

#verify it is strong no. or not
if(sum==n):
    print(f'{n} is strong no')
else:
    print(f'{n} is not strong no')