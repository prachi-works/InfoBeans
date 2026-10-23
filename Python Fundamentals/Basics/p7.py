a=int(input("Enter the first no."))
b=int(input("enter the second no."))

print(f"Before swapping a is {a} and b is {b}")
a= a^b
b=a^b
a=a^b

print(f"After swapping a is {a} and b is {b}")

