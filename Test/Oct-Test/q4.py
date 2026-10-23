# Q4. Sets — Common and Unique Elements (5 Marks)

# Given two lists, find:

# Elements common to both lists.

# Elements that appear in either list but not in both.

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]

# Expected output:

# Common elements: {30, 40}
# Unique elements: {10, 20, 50, 60, 70}
list1=[10,20,30,40,50]
list2=[30,40,60,70]
i=0
j=0
union=[]
intscton=[]
while(i<len(list1) and j<len(list2)):
    if list[i]<list[j]:
        if not union or union[-1]!=list[i]:
            union.append(list[i])
            i+=1
    elif list[i]>list[j]:
        if not union or union[-1]!=list[j]:
            union.append(list[j])
            j+=1
    else:
        i+=1
        j+=1
while(i<len(list1)):
    if union[-1]!=list[i]:
        union.append(list[i])
while(i)       
            