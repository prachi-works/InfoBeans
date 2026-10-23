# 55) WAP to print all the odd numbers between two entered numbers
start=int(input('enter the first no'))
end=int(input('enter the second no'))

print(f'\n-----All odd no.s between {start} and {end} are ------\n:')

for i in range(start,end+1):
    if i%2 != 0:
        print(i)