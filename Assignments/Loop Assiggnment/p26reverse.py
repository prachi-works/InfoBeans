#write a program to reverse a no.
n=int(input('enter the no.'))
s=0
while(n!=0):
    r=n%10
    s=s*10 + r
    n=n//10
print("reverse of a no. is",s)
