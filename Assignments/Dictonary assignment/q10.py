# 10. Merge two dictionaries. If a key exists in both dictionaries, use the
#     value from the second dictionary.
d1={'1':20,'name':'aarohi','2':30,'8':50}
d2={'1':30,'a':20,'2':90,'class':5}
# result={}
# for key,value in d1.items():
#     result[key]=value

# for key,value in d2.items():
#     result[key]=value
# print(result)

result=d1.copy()
result.update(d2)
print(result)