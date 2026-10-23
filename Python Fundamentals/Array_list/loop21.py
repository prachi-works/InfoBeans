# Q.20 Longest consecutive sequence.
# Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
#  
# Example 1:
# Input:
# N = 7
# a[] = {2,6,1,9,4,5,3}
# Output:
# 6
# Explanation:
# The consecutive numbers here
# are 1, 2, 3, 4, 5, 6. These 6 
# numbers form the longest consecutive
# subsquence.
# Example 2:
# Input:
# N = 7
# a[] = {1,9,3,10,4,20,2}
# Output:
# 4
# Explanation:
# 1, 2, 3, 4 is the longest
# consecutive subsequence.
arr=[2,6,1,9,4,5,3]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print('sorted array is',arr)
count=1
max_count=1
for i in range(1,len(arr)):
    if arr[i]==arr[i-1]+1:
        count+=1
    elif arr[i]!=arr[i-1]+1:
        count=1
    if count > max_count:
        max_count=count
print('longest consecutive sequence is length',max_count)