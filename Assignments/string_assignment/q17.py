# 16. Check whether two strings are anagrams.
# Example: "listen" and "silent" → True
s1='listen'
s2='silent'
if len(s1)!=len(s2):
    print('String are not anagram')
else:
    res={}
    for ch in s1:
        res[ch]=res.get(ch,0)+1
    print('s1:',res)

    res1={}
    for ch in s2:
        res1[ch]=res1.get(ch,0)+1
    print('s2:',res1)

if res==res1:
    print('Strings are anagram')
else:
    print('String are not anagram')