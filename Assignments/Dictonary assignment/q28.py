# 28. Create a new dictionary containing only entries whose values are greater
#     than or equal to a given threshold. Do not modify the dictionary while
#     iterating over it.

d={'a':40,'b':50,'c':70,'d':90}
th=60
res={}
for key,value in d.items():
    if d[key]>=th:
        res[key]=value
print(res)
