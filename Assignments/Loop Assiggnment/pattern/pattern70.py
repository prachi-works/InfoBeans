    #     A
    #    ABC
    #   ABCDE
    #  ABCDEFG
    # ABCDEFGHI
for i in range(1,6):
    for _ in range(9-i):
        print(' ',end='')
    for j in range(1,2*i):
        print(chr(64+j),end='')
    print()