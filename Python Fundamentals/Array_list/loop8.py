# Q.5 Find occurance of an integer number in array.
arr=[4,1,4,2,4,3]
num=4
count=0
for i in range(len(arr)):
    if arr[i]==num:
        count+=1
print(f'Occurence of integer {num} is {count}')