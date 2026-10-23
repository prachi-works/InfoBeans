# 22. Find the common keys between two dictionaries.
d1={'a': 10, 'b': 20} 
d2={'b': 5, 'c': 7}
# for key,value in d2.items():
#     if key in d1:
#         d1[key]=d1[key]+value
#         print('common keys are',d1[key])
#     else:
#         d1[key]=value
# print(d1)

for key in d2:
    if key in d1:
        print('Common key is:',key)