# 32) A	b	C	d	E	f	G	h	…… n terms 

n=int(input('enter the no.'))

for i in range(65,91):
    if(i%2 != 0):
        print(chr(i),end=' ')
    else:
        print(chr(i+32),end=' ')