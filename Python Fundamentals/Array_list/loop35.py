# 35. Write a java program to implement selection sort algoritm
arr=[64,25,12,22,11]
# Selection sort repeatedly selects the smallest or largest element and places it in the correct position.

for i in range(len(arr)):
    min_index=i

    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_index]:
            min_index=j

    arr[i],arr[min_index]=arr[min_index],arr[i]
print('sorted array :',arr )