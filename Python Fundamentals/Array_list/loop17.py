# Q.16
# Rearrange the array in alternating positive and negative items
# Given an unsorted array Arr of N positive and negative numbers. Your task is to create an array of alternate positive and negative numbers without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.

# Example 1:
# Input: 
# N = 9
# Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
# Output:
# 9 -2 4 -1 5 -5 0 -3 2
# Example 2:
# Input: 
# N = 10
# Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
# Output:
# 5 -5 2 -2 4 -8 7 1 8 0 
arr=[9,4,-2,-1,5,0,-5,-3,2]
pos=[]
neg=[]
for i in range(len(arr)):
        if arr[i]>=0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
print(pos)
print(neg)
ans=[]
for i in range(len(neg)):
    ans.append(pos[i])
    ans.append(neg[i])

for i in range(len(neg),len(pos)):
     ans.append(pos[i])
print(ans)     