# 7. Find the number of key-value pairs in a dictionary without using len().
d={
    '1':'apple',
    '22':'orange',
    '3':'banana'
}
count=0
for i in d:
    count+=1
print('The length of dictionary is',count)
