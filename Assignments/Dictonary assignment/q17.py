# 17. Count the frequency of each number in a list.
#     Example: [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}
l=[1,2,2,3,1,2]
res={}
for num in l:
    if num in res:
        res[num]=res[num]+1
    else:
        res[num]=1
print(res)