# 19. Count the frequency of every character using a dictionary.
# Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1} ,11Q also same
s='hello'
result={}

for ch in s:
    result[ch]=result.get(ch,0)+1
print(result)