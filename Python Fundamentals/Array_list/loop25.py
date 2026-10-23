# 24. Write a Java program to swap first and last element of an integer 1-d array.
n=int(input('enter the array element:'))
arr=[]
for i in range(n):
    num=int(input('enter the element'))
    arr.append(num)
   
arr[0],arr[n-1] = arr[n-1] , arr[0]
print('After swapping ',arr)