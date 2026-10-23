# 20. Remove duplicate characters while preserving their original order.
# Example: "programming" → "progamin"
s='programming'
result=''
for ch in s:
    if ch not in result:
        result+=ch
print(f'After removing duplicate characters from {s} is {result}')
        
