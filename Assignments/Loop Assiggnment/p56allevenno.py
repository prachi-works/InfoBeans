# AP to print all the even numbers between two entered numbers
start=int(input('enter the no'))
end=int(input('enter the no'))

print(f"\n----All even no between {start} and {end} are:----\n")
for i in range(start,end+1):
    if(i%2 == 0):
        print(i)