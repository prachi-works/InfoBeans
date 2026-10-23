# 24. Reverse every word without changing the word order.
# Example: "Python is easy" → "nohtyP si ysae"

s="Python is easy"
result=[]
word=s.split()
for i in range(len(word)-1,-1,-1):
    result.append(word[i])
print(' '.join(result))