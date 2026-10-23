# 5.Take input of age of 3 people by user and determine oldest and youngest among them.

age_1=int(input("Enter the age of first person:"))
age_2=int(input("Enter the age of second person:"))
age_3=int(input("Enter the age of third person:"))

if(age_1 >= age_2) and (age_1 >= age_3):
    oldest=age_1
elif(age_2 >= age_1) and (age_2 >= age_3):
    oldest = age_2
else:
    oldest= age_3

if age_1 <= age_2 and age_1 <= age_3:
    youngest= age_1
elif age_2 <= age_1 and age_2 <= age_3:
    youngest = age_2

print("Oldest person is ",oldest)
print("Youngest person is",youngest)