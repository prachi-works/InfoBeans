# 30. Find the longest common prefix among a list of strings.
# Example: ["flower", "flow", "flight"] → "fl"
words=['flower','flow','flight']
prefix=''

for i in range(len(words[0])):
    ch=words[0][i]

    flag=True
    for word in words:
        if i>=len(word) or word[i]!=ch:
            flag=False
            break
    if flag==True:
        prefix+=ch
    else:
        break
print(prefix) 
    