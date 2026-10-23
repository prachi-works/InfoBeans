'''  A
   AB
  ABC
 ABCD
ABCDE'''



for i in range(1,6):

   for _ in range(1,6-i):
         print(" ",end='')
   for j in range(1,i+1):
      print(chr(64+j),end='')
   print()
    
  
   