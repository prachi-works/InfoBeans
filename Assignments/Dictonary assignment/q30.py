
# 30. Safely retrieve a value from a deeply nested dictionary. If any key is
#     missing, return a default value such as "Unknown".
students = {
'Prachi': {'Maths': 80, 'English': 75, 'Science': 90},
'Aarohi': {'Maths': 90, 'English': 85, 'Science': 95},
'Rahul': {'English': 80, 'Science': 75}
}
name='Rahul'
subject='Marks'

print(students.get(name,{}).get(subject,'Unknown'))

# if name in students:
#     if subject in students[name]:
#         print(students[name][subject])
#     else:
#         print('unkown')
# else:
#     print('unkown')



