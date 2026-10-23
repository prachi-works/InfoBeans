# 1
# 2   2
# 3    3
# 4     4
# 5 5 5 5 5
for i in range(1,6):
        if(i==1):
            print(i)

        elif(i==5):
            print('5 5 5 5 5')

        else:
            print(i," "*(i-2)+str(i))
print()

