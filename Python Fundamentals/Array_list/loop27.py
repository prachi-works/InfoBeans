# 26. Write a Java program to find the largest and smallest element of an array.
n=int(input('enter the array element'))
arr=[]
for i in range(n):
    num=int(input('enter the element'))
    arr.append(num)
largest=arr[0]
smallest=arr[0]

for i in range(1,n):
    if arr[i]>largest:
        largest=arr[i]
    elif arr[i]<smallest:
        smallest=arr[i]
print('Largest element of array is:',largest)
print('Smallest element of array is :',smallest)