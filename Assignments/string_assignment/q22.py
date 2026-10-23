# 21. Find the most frequent character in a string.
s='aazadtiwarifromindore'
res={}
for ch in s:
    res[ch]=res.get(ch,0)+1

max_count=0
max_char=''
for ch in s:
    if res[ch]>max_count:
        max_count=res[ch]
        max_char=ch
print(res)
print('most frequent character in a string is:',max_char)
print('maximum count',max_count)