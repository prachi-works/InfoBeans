# 44) WAP to interchange first and last digit of a number

n=int(input('enter the original no'))
s=0
while(n!=0):
    r=n %10
    s=s*10+r
    n=n//10

print("Interchange of first digit and last digit is as ",s)