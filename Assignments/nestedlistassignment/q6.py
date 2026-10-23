#swap maximum and minimum sum row
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
max_sum=0
min_sum=0

max_row=0
min_row=0

for i in range(len(arr)):
    row_sum=0
    for j in range(len(arr[i])):
        row_sum=row_sum+arr[i][j]

        if row_sum>max_sum:
            max_sum=row_sum
            max_row=i

        if row_sum<min_sum:
            min_sum=row_sum
            min_row=i
#swap the rows
arr[max_row],arr[min_row] = arr[min_row],arr[max_row]  

print(arr,end='')