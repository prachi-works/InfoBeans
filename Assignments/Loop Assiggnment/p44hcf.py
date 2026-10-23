a=int(input('enter the number:'))
b=int(input('enter the number:'))

num1=a
num2=b

#find the hcf of a no.

while(a!=b):
    if a>b:
        a=a-b
    else:
        b=b-a

hcf_result=a
print(f'HCF of a {num1} and {num2} is {hcf_result}')