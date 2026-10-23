# 45) WAP to find out the sum of all the digits of a number

n=int(input('enter the no.'))

sum_of_digits=0

while(n>0):
    last_digit=n%10
    sum_of_digits=sum_of_digits + last_digit
    n=n//10

print(f"Sum of digits of a number is {sum_of_digits}")

