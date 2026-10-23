# 48) WAP to find out the factors of all the numbers between two entered numbers
start=int(input('enter the first no'))
end=int(input('enter the second no'))

print(f"\n----Factors of all even no. between{start} and {end}----\n")
for num in range(start,end+1):
    print(f"factors of {num} are: ",end=' ')

    for i in range(1,num+1):
        if(num % i == 0):
            print(i,end=' ')
    print()

    
