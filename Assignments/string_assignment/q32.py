# 31. Find the longest substring without repeating characters.
# Example: "abcabcbb" → 3 ("abc")
s='abcabcbb'
bucket=set()
max=0
left=0
right=0
for right in range(len(s)):
    ch=s[right]

    if ch in bucket:
        while s[right] in bucket:
            bucket.remove(s[left])
            left+=1
    bucket.add(s[right])
    
    if (right-left+1)>max:
        max=right-left+1
print(max)