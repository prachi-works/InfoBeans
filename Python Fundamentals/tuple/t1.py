#creating tuples
t=(1,2,3,4)
print(t)
print(type(t))

#using typle constructor
t1=([1,2,3])
print(type(t))

#without parantheses
t=1,2,3,4
print(type(t))

#empty tuple
t=()
print(type(t))

t=(10)
print(t)
print(type(t))

#for single element we have to separate it by ,
t=(10,)
print(t)
print(type(t))

#Accesing tuple element
t=(10,20,30)
print(t[0])
print(t[-1])

#slicing
print(t[1:3])

#Tuple immutability
t=(10,20,30)
# t[1]=50   
# TypeError: 'tuple' object does not support item assignment
print(t)

#tuple itself is immutable ,but if contains mutable object ,that object can change
t=([1,2],3)
t[0].append(4)
print(t)

#tuple packing and unpacking
t=10,20,30
#packig:means assigning value into a single variable 
print(t)

#unpacking means assigning value into different variables
a,b,c=10,20,30
print(a)

#extended unpacking using *
a=[10,20,30,40]
x,*y = a
print(x)
print(y)


s,*z=(1,2,3,4)
print(s)
print(z)

a,*b,c=(1,2,3,4,5)
print(a)
print(b)
print(c)
