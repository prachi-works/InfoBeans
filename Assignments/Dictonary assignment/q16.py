# 16. Count the frequency of each character in a string.
#     Example: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
str=input('enter a string:')
result={}
for ch in str:
    if ch in result:
        result[ch]=result[ch]+1
    else:
        result[ch]=1
print(result)
# enter a string:aazad
# {'a': 3, 'z': 1, 'd': 1}