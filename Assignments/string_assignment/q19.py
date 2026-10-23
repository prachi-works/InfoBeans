# 18. Find the first repeating character.
# Example: "programming" → r
s='programming'
result={}
for ch in s:
    result[ch]=result.get(ch,0)+1
for ch in s:
    if result[ch] != 1:
        print('First non repeating character is',ch)
        break
print(result)