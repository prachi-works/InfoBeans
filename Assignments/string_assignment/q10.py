# 9. Find the first and last character of a string.
s='prachi'
for i in range(len(s)):
    if i==0:
        print('First character:',s[0])
    if i==len(s)-1:
        print('Last character :',s[i])

#without slicing 
s='hello'
first_chr=''
last_chr=''
for ch in s:
    if first_chr=='':
        first_chr=ch
    last_chr=ch
print('First character:',first_chr)
print('Last character:',last_chr)