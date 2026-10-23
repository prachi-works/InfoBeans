# Q2. Loops — Prime Numbers (5 Marks)

# Write a program to print all prime numbers between 1 and 100. Do not use any built-in prime-checking function.

# Expected output: 2, 3, 5, 7, 11, ... 97
for n in range(1,100):
    i=2
    while(i<=n//2):
        if n%i==0:
            break
        i+=1
    if(i>n//2 and n>1):
        print(n,end=' ')
  