# 9. Find the key associated with the largest value in a dictionary.
student={
    'name':'prachi',
    'age':20,
    'mark':90,
    'hmark':33
}
high=float("-inf")
for key,value in student.items():
    if(isinstance(value,(int,float))):
        if student[key] > high:
            high=value

print('maximum value is',high)