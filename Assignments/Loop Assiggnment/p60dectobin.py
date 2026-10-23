# 58) WAP to convert decimal number into binary number without using array
decimal_no=int(input('enter the number:'))
binary_no=0
base=1
temp=decimal_no

while(temp>0):
    r=temp%2
    binary_no=binary_no+(r*base)
    base=base*10
    temp=temp//2

print(f"The binary equivalent of the {decimal_no} is {binary_no}")