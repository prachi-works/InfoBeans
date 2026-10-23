# 27. Find all duplicate characters and their frequencies.
s='aabbcccddd'
res={}
for ch in s:
    res[ch]=res.get(ch,0)+1

for ch in res:
    if res[ch]>1:
        print(ch,res[ch])

# a 2
# b 2
# c 3
# d 3