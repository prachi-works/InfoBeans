# 14. Copy a dictionary into another dictionary. Explain whether changing a
#     nested object in the copy can affect the original.
dict1 = {
    'name': 'prachi',
    'marks': [80, 90, 95]
}

dict2=dict1.copy()

print('original dictionary',dict1)
print('copied dictionary',dict2)

dict2['marks'][0]=50
print('After changing the object:')
print('original dictionary is',dict1)
print('copied dictionary',dict2)
