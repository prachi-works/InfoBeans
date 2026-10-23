# A
# BCD
# EFGHI
# JKLMNOP
num=65
for i in range(5):
    for j in range(1,i*2):
        print(chr(num),end='')
        num+=1
    print()
