# Q.2 Find minimum and maximum element in array
arr=[5,2,3,1,4]
min=arr[0]
max=arr[0]
for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
    elif arr[i] > max:
        max = arr[i]
print(f"{max} and {min}")