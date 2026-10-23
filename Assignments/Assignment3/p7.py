# 7. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

no_of_class_held=int(input("Enter the no. of class held is"))
no_of_class_attended=int(input("Enter the no. of class attended"))
percentage_of_class_attended= (no_of_class_attended/no_of_class_held) * 100

print("Attendence Percentage:",percentage_of_class_attended,"%")

if(percentage_of_class_attended < 75):
    print("Not allowed in exam")
else:
    print("Allowed in exam")
