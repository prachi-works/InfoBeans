# 11. Count how many times a particular character occurs.
s='aaabbccddefgghee'
result={}
for ch in s:
    result[ch]=result.get(ch,0)+1
print(result)
# {'a': 3, 'b': 2, 'c': 2, 'd': 2, 'e': 3, 'f': 1, 'g': 2, 'h': 1}