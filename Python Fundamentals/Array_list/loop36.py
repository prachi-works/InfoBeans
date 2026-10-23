# 36. Write a java program to implement bubble sort algorithm

arr=[5,2,3,8,1]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print('sorted array :',arr)


