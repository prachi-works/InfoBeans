# 23. Reverse the order of words in a sentence.
# Example: "Python is easy" → "easy is Python"
s='Python is easy'
words=s.split()
result=[]

for word in words:
    rev=''
    for ch in word:
        rev=ch+rev
    result.append(rev)
print(' '.join(result))