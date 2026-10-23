# # 25. Given a nested dictionary of students and their subject marks, calculate
# #     each student's total marks and find the topper.
# students = {
#     'Prachi': {'Maths': 80, 'English': 75, 'Science': 90},
#     'Aarohi': {'Maths': 90, 'English': 85, 'Science': 95},
#     'Rahul': {'Maths': 70, 'English': 80, 'Science': 75}
# }

# result = {}

# for key,value in students.items():
#     sum=0
#     for k1,v1 in value.items():
#         sum = sum + v1
#         result[key] = sum

# print(result)

# high = 0
# for key,value in result.items():
#     if value>high:
#         high = value
#         topper = key
# print(topper,high)


























students = {
    'Prachi': {'Maths': 80, 'English': 75, 'Science': 90},
    'Aarohi': {'Maths': 90, 'English': 85, 'Science': 95},
    'Rahul': {'Maths': 70, 'English': 80, 'Science': 75}
}
res={}
for key,value in students.items():
    sum=0
    for k1,v1 in value.items():
        sum=sum+v1
        res[key]=sum
print(res)

high=0
for key,value in res.items():
   if value>high:
       high=value
       topper=key
print(topper,high)
        


