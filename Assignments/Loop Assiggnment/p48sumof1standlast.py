# 46) WAP to find out the sum of first and last digit of a user entered number 

n=int(input('enter the number'))

temp=n

#get the last digit by % remainder

last_digit=temp%10

#use loop for first one is extract
while temp>= 10:
    temp=temp//10

first_digit=temp

#sum fo first and last digit is
digit_sum= first_digit+last_digit
print(f'So the sum of first and last digit is {digit_sum}')
