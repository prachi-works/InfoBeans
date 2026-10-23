# 52) WAP to find out all the Armstrong numbers between two entered numbers
start=int(input('enter the 1st no:'))
end=int(input('enter the 2nd no:'))

print(f'\n----All Armstrong No between two number----\n')

for num in range(start,end+1):
    temp1=num
    length=0
    while(temp1!=0):
        length+=1
        temp1=temp1//10

    temp2=num
    s=0
    while(temp2!=0):
        r=temp2%10
        s=s+r**length
        temp2=temp2//10
        
    if(s==num):
        print(num)