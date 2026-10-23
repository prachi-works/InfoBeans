    #     1
    #    123
    #   12345
    #  1234567
    # 123456789

for i in range(1,6):
   for _ in range(9-i):
      print(" ",end='')
   for j in range(1,2*i):
      print(j,end='')
   print()