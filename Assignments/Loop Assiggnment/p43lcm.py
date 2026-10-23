# 41) WAP to find out LCM of a number
a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))

#save original no.
num1=a
num2=b

#loop run until both number are equal
while(a!=b):
    if a>b:
        a=a-b
    else:
        b=b-a
gcd=a

#calculate the lcm
lcm= (num1 * num2)//gcd
print(f'The lcm of number{num1} and {num2} is {lcm}')



