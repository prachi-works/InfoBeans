# 43) WAP to convert binary number into decimal number

binary_num=1011
base=1
temp= binary_num
decimal_num=0

while(temp>0):
    last_digit=temp%10
    decimal_num=decimal_num+(base * last_digit)
    base=base*2
    temp=temp//10
print("The decimal number is: ",decimal_num)


