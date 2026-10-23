# 6. Remove a key from a dictionary using pop(). Handle the case where the
#    key does not exist.
student={
    'name':'prachi',
    'age': 21,
    'marks':50}
student.pop('age')
print(student)
# student.get('age',Not Found)
print(student.get('country'))   #for handle the case where key does not exists we use get function which give output if value not present in is NOne
# print(student.popitem())     ('marks', 50)this would be the ans,popitem remove from the last
# print(student)