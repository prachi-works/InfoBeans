#slicing 
l=[10,20,30,40,50,60,70,80,90,100]

print(l[2:])   #start with  to the end

print(l[1:5])

print(l[:5]) 

print(l[1:9:2])

print(l[: :-1])

print(l[1:100])  #if there is not any no. of this index it add in last in step is positive

print(l[7:3:-1])

print(l[-8:-4])

for i in range(len(l)):
    print(f"Index : {i} : value : {l[i]}")


