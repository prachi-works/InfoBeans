#  WAP to find out the factors of a number.
i=1
n=int(input("Enter the number:"))
print("The factors of the number are :")

while(i <= n):
    if(n % i == 0):
        print(i,end=" ")
    i+=1