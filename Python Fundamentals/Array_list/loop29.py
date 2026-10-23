# 29. Suppose a one-dimensional array AR containing integers is arranged in ascending order. Write a java program to search for an integer from AR with the help of Binary search method,
ar=[10,20,30,40,50] #sorted array 
target=40
left,right=0,len(ar)-1

while left <= right:
    mid = (left+right)//2
    if ar[mid] == target:
        print('element found at index:',mid)
        break
    elif ar[mid]<target:
        left=mid+1
    else:
        right = mid-1
