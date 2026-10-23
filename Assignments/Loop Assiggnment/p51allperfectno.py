# 49) WAP to find out all the perfect numbers between two entered numbers
start=int(input('enter the no.'))
end=int(input('enter the no.'))

print(f"\n----All Perfect Number between {start} and {end}----\n")

for num in range(start,end+1):
    

    if num <= 0:
        continue

    factor_sum=0

    for i in range(1,num):
        if num % i ==0:
            factor_sum+=i
    if factor_sum==num:
            print(num)

            