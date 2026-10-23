# 19. Find all duplicate elements in a list and their frequencies.
l=[1,3,1,2,4,3,5]
res={}
for element in l:
    if element in res:
        res[element]=res[element]+1
    else:
        res[element]=1
for element in res:
    if res[element]>1:
        print('Duplicate elements are:',element)
print(res)