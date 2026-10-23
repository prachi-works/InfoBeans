# 26. Find the longest word in a sentence.
s='Python is easy'
words=s.split()
longest=''
for word in words:
    if len(word)>len(longest):
        longest=word
print('Longest word is ',longest)
print('length of longest word is',len(longest))