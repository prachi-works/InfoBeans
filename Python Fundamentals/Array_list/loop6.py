# Q.7 Sub array with given sum
# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

# Example 1:
# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.
arr=[1,2,3,7,5]
cs=0
left=0
right=0
target=12

for right in range(len(arr)):
    cs += arr[right]

    while cs>target and left <=right:
        cs -= arr[left]
        left += 1
    if cs == target:
        print(f'[{left+1},{right+1}]')
        break
else:
    print(f'No subarray exist')