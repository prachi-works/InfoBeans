#     #
#    *#*
#   **#**
#  ***#***
# ****#****
for i in range(1,6):
   for _ in range(5-i):
      print(" ",end='')
   for j in range(1,2*i):
      if j==i:
         print('#',end='')
      else:
        print('*',end='')
      
   print()