import sys
l1=[10,20,30]

print(f"Data:{l1}")
print(f"Lenght:{len(l1)}")
print(f"Size:{sys.getsizeof(l1)}")

l1.append(100)
print(f"After append data append{l1}")
print(f"Length:{len(l1)}")
print(f"siize:{sys.getsizeof(l1)}")

l1.append(200)
print(f"After append data append{l1}")
print(f"Length:{len(l1)}")
print(f"siize:{sys.getsizeof(l1)}")#show size of 120 because of overallocation

