# 29. Remove a particular character from a string without using replace().
s='aashutosh'
s=list(s)

for i in range(len(s)):
    if s[i]=='a':
        s[i]=''
s=''.join(s)
print(s)


#another method*****
res=''
for ch in s:
    if ch!='a':
        res+=ch
print(res)