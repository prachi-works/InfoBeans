
# 11. Create a dictionary from two lists: one list contains keys and the
#     other contains values. Do not use zip().
key=['1','work','business','pincode']
value=[20,'on-site',20,481331]

dict={ }
for i in range(len(key)):
    dict[key[i]]=[value[i]]
print(dict)