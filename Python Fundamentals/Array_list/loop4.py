#sorting of array
arr=[2,5,1,3,9,7]
for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:     #if want descending change it as if arr[j] < arr[j+1]
            arr[j+1],arr[j]=arr[j],arr[j+1]
print(arr)

