# 25. Write a Java program to reverse the element of an integer 1-D array. 
arr=[10,20,30,40,50,60]
j=len(arr)-1
for i in range(len(arr)//2): #only need to handle half of the array because every swap handles two elements
    arr[i],arr[j]=arr[j],arr[i]
    j-=1
print('Reversed array is :',arr)
