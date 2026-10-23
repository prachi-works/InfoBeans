#   16) …... -6	-3	0	3	6	9	……. n terms [where n is even] where n is divisible of 3

n=int(input('Enter the value of n:'))

if n%3 == 0:
    for i in range(-n,n+1,3):
        print(i,end=' ')
    

