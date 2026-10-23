# 7. Convert lowercase characters to uppercase without using upper().
s = "inDor434e"        # => "INDOR434E"
result=''
for ch in s:
    ascii=ord(ch)
    if ascii>=97 and ascii<=122:
        result+=chr(ascii-32)
    else:
        result+=ch
print(f'Lowercase {s} into Uppercase are {result}')

