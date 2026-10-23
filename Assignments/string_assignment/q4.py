# 4. Count uppercase letters, lowercase letters, digits, and special characters.
s='InDoreMaD8Y9##APrad@esh'
uc=lc=dc=sc=0
for ch in s:
    ascii=ord(ch)
    if ascii>=65 and ascii<=90:
        uc+=1
    elif ascii>90 and ascii<=120:
        lc+=1
    elif ascii>=48 and ascii<=57:
        dc+=1
    else:
        sc+=1
print(f'Uppercase letter are {uc}')
print(f'Lowercase letter are {lc}')
print(f'Digits are {dc}')
print(f'Specilal characters are {sc}')