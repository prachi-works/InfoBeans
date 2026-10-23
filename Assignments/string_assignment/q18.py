#What is the first non-repeating character?
s='swiss'
result={}
for ch in s:
    result[ch]=result.get(ch,0)+1
for ch in s:
    if result[ch]==1:
        print('First non repeating element is:',ch)
        break
print(result)