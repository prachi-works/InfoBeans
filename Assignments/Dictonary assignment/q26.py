# 26. Find the second-largest distinct value in a dictionary.

d={'a':1,'b':2,'c':2,'d':4}
values=[]
for value in d.values():
    if value not in values:
        values.append(value)
values.sort()
print('Second-largest distinct value is ',values[-2])














        