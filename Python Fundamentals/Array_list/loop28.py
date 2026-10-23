# 27 P is one-dimensional array of integers. Write a Java program search for a data VAL from P. If VAL is present in the array then “element found ” otherwise “element not found” should be displayed.  
P=[4,5,1,9,2]
val=1
found=False
for i in range(len(P)):
    if P[i]==val: #linear search
        found=True
        break
if found==True:
    print('element found')  
else:
    print('element not found')