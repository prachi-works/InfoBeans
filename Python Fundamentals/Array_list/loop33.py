# 33. Write a java program to impelment binary search algorithm
arr=[5,6,7,8,9,10]
target=8
left,right=0,len(arr)-1
while left<right:
    mid= (left+right) //2
    if arr[mid]==target:
        print('element found at index',mid)
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print('element not found')

