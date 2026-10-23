# Write a program that accepts an integer and checks whether it is a Harshad number.

# A number is a Harshad number if it is divisible by the sum of its digits.

# Example:

# Input: 18

# Output: Harshad Number (18 is divisible by 1 + 8 = 9)
n=int(input('enter a number:'))
temp=n
sum=0
while(temp>0):
    rem=temp%10
    sum+=rem
    temp//=10
if n%sum==0:
    print('Its is a Harshad number')
else:
    print('it is not a harshad number')
