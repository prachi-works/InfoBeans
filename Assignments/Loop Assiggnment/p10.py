# 9) WAP to print N even numbers. ( it print even no.s which we give ex: if we give 5 it print 5 even no.)

N=int(input('enter the n no.s'))

first_even_n=2
count=0

while(count < N):
    print(first_even_n,end=' ')
    first_even_n+=2
    count+=1 

