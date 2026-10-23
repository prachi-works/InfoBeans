x=[10,20,30,40,50]
print(f'First element of :{x}')
print(f'length of element :{len(x)}')
print(f'type of list:{type(x)}')

#index based question
for i in range(len(x)):
    print(f'Index:{i} Value:{x[i]}')

#Element wise access
for element in x:
    print(f'{element}')