# *
# **
# *@*
# *@@*
# * * * * *
for i in range(1,6):
    # if i==1:
    #     print('*')
    # elif i==2:
    #     print('**')
    # elif i==3:
    #     print("*@*")
    # elif i==4:
    #     print('*@@*')
    # else:
    #     print('* * * * *')

    for j in range(1,i+1):
        for j in range(1,i+1):
            if i>j and j!=1 and i!=5:
                print('@',end='')
            else:
                print('*',end='')
        print()