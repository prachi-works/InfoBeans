# 22. Find the second most frequent character.
s='aazadtiwarifromindore'
res={}
for ch in s:
    res[ch]=res.get(ch,0)+1

# first=max(res,key=res.get)
# res.pop(first)

# second=max(res,key=res.get)
# print(res)
# print(second,res[second])

max_count=0
for ch in s:
    if res[ch]>max_count:
        max_count=res[ch]

second_count=0
second_char=''
for ch in s:
    if res[ch]<max_count and res[ch]>second_count:
        second_count=res[ch]
        second_char=ch
print(res)
print(second_char)
print(second_count)