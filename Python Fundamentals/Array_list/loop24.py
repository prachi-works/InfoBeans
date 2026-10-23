# 23. Write a Java program to find the sum and average of one dimensional integer array. \
n=int(input('enter the element of an array:'))
arr=[]
for i in range(n):
    num=int(input('enter the element:'))
    arr.append(num)

total_sum=0
for i in range(len(arr)):
    total_sum+=arr[i]

avg=total_sum/len(arr)
print(f'Total sum of the array is {total_sum}')
print(f'Average of one dimensional array is {avg}')