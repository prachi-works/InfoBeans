# 14. Remove all digits from a string.
s = "P1y2t3h4o5n"
res=""
for ch in s:
    if not ch.isdigit():
        res+=ch
print(res)


#count no digit
count=0
for ch in s:
    if ch.isdigit():
        count+=1
print(count)

#count both digit and alphabets
digit_count=0
alpha_count=0
for ch in s:
    if ch.isdigit():
        digit_count+=1
    elif ch.isalpha():
        alpha_count+=1
print(digit_count)
print(alpha_count)            
