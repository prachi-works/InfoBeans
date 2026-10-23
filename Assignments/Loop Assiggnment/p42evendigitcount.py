# 40) WAP to count no. Of even and odd digits in a number

n=int(input('enter the no:'))
even_count=0
odd_count=0

temp=n

while temp>0:
    r=temp%10

    if(r%2==0):
        even_count+=1
    else:
        odd_count+=1

    temp=temp//10
print("Even digits:",even_count)
print("Odd digits:",odd_count)
    




