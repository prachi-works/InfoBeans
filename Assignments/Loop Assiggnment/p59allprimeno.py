# 57) WAP to print all the prime numbers between two entered numbers

start=int(input('enter 1st no.'))
end=int(input('enter 2nd no.'))

print('\n----all prime number between two entered numbers is----\n')

for num in range(start,end+1):

    i=2
    while(i<=num//2):
        if(num%i == 0):
            break
        i+=1
    if(i>num//2 and num>1):
        print(num)
