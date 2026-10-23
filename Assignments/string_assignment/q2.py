# 2. Check whether a string is a palindrome.
# s='aajaa'
# l=list(s)
# left=0
# right=len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# result="".join(l)
# print(result)  
# if result==s:
#     print('palindrome no.')
# else:
#     print('not palindrome no.')

s='NITIN'
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print('not palindrome')
        break
    left+=1
    right-=1
else:
    print('Palindrome')

