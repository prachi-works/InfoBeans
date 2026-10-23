# 25. Check whether a string contains only digits without using isdigit().
s='a1234b'
flag=True
for ch in s:
    if ch<'0' or ch>'9':          #if ord(ch) < 48 or ord(ch) > 57:
        flag=False
        break
if flag==True:
    print('Only digits')
else:
    print('not only digits present')

