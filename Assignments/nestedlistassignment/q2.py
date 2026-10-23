arr=[[1,4,5],
     [6,7,8],
     [9,10,11]]
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if row<col:
            print(arr[row][col],end=' ')