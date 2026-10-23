# 10. Replace every space with a hyphen (-).
s='Hello I am Your Partner'
# s=s.replace(' ','-')
# print(s)
#without replace
s=list(s)
for i in range(len(s)):
    if s[i]==' ':
        s[i]='-'
s=''.join(s)
print(s)