# 5. Count the number of words in a sentence.
s='Hi I am a Dancer'
# l=s.split()
# print('Count the number of words in a sentence',len(l))
#Another way is 
word=1
for ch in s:
    if ch == ' ':
        word+=1
print(f'total words are:{word}')