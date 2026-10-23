# Q.5 Find the kth largest and kth smallest element in array.
#first sorting
arr=[1,4,3,8,7,9]
k=2
for i in range(len(arr)):
    for j in range(len(arr)-1-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(f"{k}nd smallest element is {arr[k-1]}")
print(f'{k}nd largest element is {arr[-k]}')