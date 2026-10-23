#reverse each row
arr=[[4,3,2,1],
     [9,8,6,5],
     [8,7,6,2]]
for i in range(len(arr)):
    for j in range(len(arr[i])-1,-1,-1):
        print(arr[i][j],end=' ')

    print()

# for i in range(len(arr)):
#     left=0
#     right=len(arr[i])-1
#     while left<right:
#         arr[i][left],arr[i][right]=arr[i][right], arr[i][left]


#         left+=1
#         right-=1
# print(arr,end=' ')