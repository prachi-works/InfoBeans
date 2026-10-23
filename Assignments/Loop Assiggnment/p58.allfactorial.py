start=int(input('enter the no.'))
end=int(input('enter no.'))

print(f'\n----All Factorial no between {start} and {end} is')

for num in range(start,end+1):
    fact=1
    i=1
    while(i<=num):

        fact= fact *i

        i += 1

    print(f'Factorial of {num} is {fact}')
   