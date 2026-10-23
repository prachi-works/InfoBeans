# 8. Remove all spaces from a string.
s=' HI Guys! I am Your Friend'
print(s)
s=s.replace(' ','')
print(s)

#Without replace
# l=list(s)
# result=''
# for i in range(len(l)):
#     if l[i] != " ":
#         result+=l[i]
# print(result)

s=list(s)
for i in range(len(s)):
    if s[i] == ' ':
        s[i]=''
s=''.join(s)
print(s)