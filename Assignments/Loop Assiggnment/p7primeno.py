#check whether the entered no. is prime or not
n=int(input("Enter the number:"))

i=2 #becaus 2 is the smallest prime no.

while(i <= n//2):
    if(n % 2 == 0):
        break
    i+=1
if(i >= n//2 and n >1):
    print("The given no. is prime")
else:
    print("The given no. is not prime")
        