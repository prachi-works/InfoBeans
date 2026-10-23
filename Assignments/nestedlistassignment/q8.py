#multiplication between two matrics
a=[[1,2],
   [3,4]]

b=[[1,2],
   [3,4]]

result=[[0,0],
        [0,0]]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j]=result[i][j]+a[i][k]*b[k][j]
print(result,end='')