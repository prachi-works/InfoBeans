# 20. Reverse a dictionary so that values become keys and keys become values.
#     Assume all values are unique.
d={'1':'name','101':2,'Roll_no':3}
# Expected output:{'name': '1', 2: '101', 3: 'Roll_no'}
res={}

for key,value in d.items():
    res[value]=key
print(res)