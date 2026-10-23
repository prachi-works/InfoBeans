# 3. Count the number of vowels and consonants in a string.
s='IndoreMP'
l=list(s)
vowel='aeiouAEIOU'
vowel_count=cons_count=0
for i in range(len(l)):
    if l[i] in vowel:
        vowel_count+=1
    else:
        cons_count+=1
print(f'vowel_count is {vowel_count}')
print(f'consonat count is {cons_count}')