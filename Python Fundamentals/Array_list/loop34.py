#linear search
arr=[1,2,3,4,5]
key=3
found=False
for i in range(len(arr)):
    if arr[i]==key:
        found=True
        break
if found==True:
    print('element found ')
else:
    print('element not found')