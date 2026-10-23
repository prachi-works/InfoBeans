# 12. Print all keys, all values, and all key-value pairs of a dictionary.
employee={'1':101,'2':'prachi','3':'rudraksh'}
for key in employee.keys():
    print(key)
for value in employee.values():
    print(value)
for key,value in employee.items():
    print(f'{key}:{value}')