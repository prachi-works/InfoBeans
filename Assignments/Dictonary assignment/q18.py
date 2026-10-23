# 18. Find the first non-repeating character in a string using a dictionary.
str=input('enter a string:')
result={}
for ch in str:
    if ch in result:
        result[ch]=result[ch]+1
    else:
        result[ch]=1
for ch in str:
    if result[ch]==1:
        print('first non repeating value is',ch)
        break
print(result)