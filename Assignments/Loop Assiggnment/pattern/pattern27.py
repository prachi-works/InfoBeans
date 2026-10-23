# 1
# 10
# 1 1
# 1  0
# 10101

for i in range(1,6):
        if i==1:
            print('1')
        elif i==2:
              print('10')
        elif i==5:
              print('10101')
        else:
              print('1'," "*(i-2)+str(i%2))
              

