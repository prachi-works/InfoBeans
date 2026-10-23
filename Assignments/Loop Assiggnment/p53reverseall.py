# 51) WAP to reverse all the numbers between two entered numbers

start=int(input('enter the first number'))
end=int(input('enter the second number'))

print(f"\n----Reverse all the number between two number {start} and {end}----\n")

for num in range(start,end+1):

    temp=num
    s=0
    while(temp>0):

        r = temp % 10
        s = s * 10 + r
        temp = temp // 10

    print(f"Origninal:{num} --> Reversed: {s}")
