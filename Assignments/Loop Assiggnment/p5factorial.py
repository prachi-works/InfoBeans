# 5) WAP to find out the factorial of a number.

n=int(input("Enter the number:"))
fact=1
i=1
while(i<= n):
    fact = fact * i
    i+=1
print("Factorial of no. is",fact)