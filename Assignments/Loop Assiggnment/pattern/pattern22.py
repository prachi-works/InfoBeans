# A
# AB
# A C
# A  D
# ABCDE
for i in range(1,6):
    if i == 1:
        print('A')
    elif i==2:
        print('AB')
    elif i==5:
        print('ABCDE')
    else:
        print('A'+" "*(i-2)+chr(65+i-1))
   
