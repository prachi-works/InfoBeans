# 53) WAP to print all the strong numbers between two entered numbers

import math

start=int(input('enter the no'))
end=int(input('enter the no'))
print(f'\n----All strong number between {start} and {end}----\n')

for num in range(start,end+1):
    temp=num
    s=0
    while(temp>0):
        r = temp%10
        s += math.factorial(r)
        temp = temp//10
    if(s==num):
        print(num)

    # from 1 to 100,000, you would only ever find four of them: 1, 2, 145, and 40585!