ch=97

for i in range(1,6):
    if(i==1):
        print(chr(ch))
        ch+=1

    elif(i==2):
        print(chr(ch)+chr(ch+1),sep='')
        ch+=2

    elif(i==3):
        print(chr(ch)+" "+chr(ch+2))
        ch+=3
    elif(i==4):
        print(chr(ch)+' '+chr(ch+3))
        ch+=4
    else:
        print('klmno')
    
