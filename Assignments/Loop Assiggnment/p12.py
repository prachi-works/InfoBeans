#  WAP to print  upto N odd numbers.

n=int(input('Enter the no.'))

i=1

while(i <= n):
    if(i%2 != 0):
        print(i)
    i+=1