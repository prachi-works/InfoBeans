# Q.9 Find the Union and Intersaction of two sorted array.
# Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays. 
# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.
# Example 1:
# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3
# Output: 
# 5
# Explanation: 
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.
arr1=[5,8,8,9,11,12]
arr2=[3,8,10,12,15]
i=0
j=0
union=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        if not union or union[-1]!=arr1[i]:
         union.append(arr1[i])
        i+=1
    
    elif arr1[i]>arr2[j]:
        if not union or union[-1]!=arr2[j]:
            union.append(arr2[j])
            j+=1
    else: #arr1[i]==arr2[j]
        if not union or union[-1]!=arr1[i]:
            union.append(arr1[i])
        j+=1
while i<len(arr1):
    if union[-1] != arr1[i]:
        union.append(arr1[i])
    j+=1
    i+=1
while j<len(arr2):
    if not union or union[-1] != arr2[j]:
        union.append(arr2[j])
    j += 1

print(union)
print("Count:", len(union))