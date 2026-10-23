# Write a Python program that accepts a positive integer N and prints:

# Sum of all digits
# Number of digits
# Largest digit
# Smallest digit
# Whether the number is a palindrome

# Example:

# Enter number: 12321

# Sum of digits: 9
# Number of digits: 5
# Largest digit: 3
# Smallest digit: 1
# Palindrome: Yes

# Restriction: Do not convert the number into a string.
n=int(input('enter the positive no.'))
temp=n
rev=0
while(temp>0):
    r=temp%10
    rev=rev*10+r
    n=temp//10
print(f'reverese of no. is {rev}')
if (rev==n):
    print('yes it is palindrome')
else:
    print('not palindrome')




