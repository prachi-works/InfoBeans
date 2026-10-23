#write a program to print a no. is palindrone or not
n=int(input('enter the no.'))
temp=n
s=0

while(n!=0):
    r=n%10

    s = s * 10 + r
    n=n//10

print(s)

if(temp == s):
    print("Palindrome no")
else:
    print("not palindrome no")
