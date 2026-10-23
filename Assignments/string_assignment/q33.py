# 32. Find the longest palindromic substring.
# Example: "babad" → "bab" or "aba"

s='babad'
longest=''

# for i in range(len(s)):
#     for j in range(i,len(s)):
#         sub=s[i:j+1]

#         if sub==sub[::-1]:
#             if len(sub) > len(longest):
#                 longest = sub
# print(longest)

#by Brute force approach
if len(s)==0 or len(s)==1:
    print('String must have two character....')
else:
    max_len=0
    for i in range(len(s)-1):
        for j in range(i,len(s)):
            palindrom=s[i:j+1]

            l=list(palindrom)
            left=0
            right=len(l)-1
            while left<right:
                l[left],l[right]=l[right],l[left]
                left+=1
                right-=1
            temp=''.join(l)

            if palindrom==temp:
                if max_len<len(palindrom):
                    max_len=len(palindrom)
                    longest=palindrom
print(max_len)
print(longest)