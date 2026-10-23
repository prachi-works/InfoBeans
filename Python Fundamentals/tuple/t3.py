#Iterating Tuple

# t=(20,40,50,60)
# for i in range(t):
#     print(i)

#indexing tuple
t=(20,40,50)
for i in range(len(t)):
    print(t[i])

#concatenation
t1=(1,2)
t2=(3,4)
print(t1+t2)

#reptition
print(t1*3,t2*2)

#nested tuple
t=((1,2),(3,4))
print(t[0])
print(t[1][1])

#membership testing
t=(10,20,30)
print(20 in t)
print(30 in t)

