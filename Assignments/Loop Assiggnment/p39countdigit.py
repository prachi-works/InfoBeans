# 35) WAP to count number of digits

n=int(input('enter the no'))
count=0
temp=abs(n) #for not negative no.

if(temp == 0):
    count = 1
else:
    while(temp > 0):
        temp//=10
        count+=1
print(count)

# x=12345
# digit_count=len(str(abs(x)))
# print(digit_count)