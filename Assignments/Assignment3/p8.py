# 8. Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.


no_of_class_held=int(input("Enter the no. of class held is"))
no_of_class_attended=int(input("Enter the no. of class attended"))
percentage_of_class_attended= (no_of_class_attended/no_of_class_held) * 100

medical_cause=input("Do you have an medical cause? (yes/no):")

print("Attendence Percentage:",percentage_of_class_attended,"%")


if(percentage_of_class_attended >= 75):
    print("Allowed to sit in exam")
elif(medical_cause.lower()=='yes'):
    print("Allowed to sit in exam due to medical cause")
else:
    print("Not allowed to sit in the exam")