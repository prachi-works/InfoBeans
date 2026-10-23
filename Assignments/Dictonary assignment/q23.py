# 23. Sort a dictionary by its values in ascending order.
d={'a':50,'b':40,'c':30,'d':20,'e':10}
res={}
values=sorted(d.values())
for value in values:
    for key in d:
        if d[key]==value:
            res[key]=value
print(res)
# d = {'a': 50, 'b': 20, 'c': 40, 'd': 10}
