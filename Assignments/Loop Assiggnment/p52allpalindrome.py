# 49) WAP to find out all the palindrome numbers between two entered numbers
start=int(input('enter the number'))
end=int(input('enter the number'))

print(f'\n----All Palindrome No----\n')

for num in range(start,end+1):
    temp=num
    s=0
    while temp>0:
        r=temp%10
        s=s*10+r
        temp=temp//10
    if(s==num):
        print(num)