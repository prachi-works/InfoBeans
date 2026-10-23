# convert uppercase characters to lowercase without using lower()?
s='NEPALindia_havEGooDBond'
result=''
for ch in s:
    ascii=ord(ch)
    if ascii>=65 and ascii<=90:
        result+=chr(ascii+32)
    else:
        result+=ch
print('Lowercase:',result)