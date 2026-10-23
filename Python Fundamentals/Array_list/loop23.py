# Q.22) Java program to find nearest lesser and greater element in array
# Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.
# Example:
#     Input:
#     Enter the number of elements for the arrray : 3  
 
#     Enter the elements for array_1.. 
#     array_1[0] : 1   
#     array_1[1] : 2   
#     array_1[2] : 3   
 
#     Enter the number : 2 
 
#     Output:
#     Element lesser than 2 is : 1 
#     Element greater than 2 is : 3
n=int(input('Enter the number of elements for the array:'))
arr=[]

for i in range(n):
    num = int(input(f'array_1[{i}]:'))
    arr.append(num)
target = int(input('Enter the number:'))
lesser=None
greater=None

for  i in range(n):
    if arr[i]<target and (lesser==None or arr[i]>lesser): #example if arr[i]=1<2 true and in or condition if one is true it will store the value
        lesser = arr[i]
    elif arr[i]>target and (greater==None or arr[i]<greater):
        greater=arr[i]
print(f'Element lesser than {target} is {lesser}')
print(f'Element greater than {target} is {greater}')

