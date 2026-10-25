# 1. Write a program to reverse a string without using slicing ([::-1]). By function
def reverse():
    s='hello'
    l=list(s)
    left=0
    right=len(l)-1
    while(left<right):
        l[left],l[right]=l[right],l[left]
        left+=1
        right-=1
    print(''.join(l))
reverse()
