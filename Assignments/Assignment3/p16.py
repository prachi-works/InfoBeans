# 16. Write a Java program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.          Calculate percentage and grade according to following: 
# 	Percentage >= 90% : Grade A 
# 	Percentage >= 80% : Grade B 
# 	Percentage >= 70% : Grade C 
# 	Percentage >= 60% : Grade D 
# 	Percentage >= 40% : Grade E 
# 	Percentage < 40% : Grade F

Physics=int(input("Enter the physics marks:"))
Chemistry=int(input("Enter the chemistry marks:"))
Biology=int(input("Enter the biology marks:"))
Mathematics=int(input("Enter the mathematics marks:"))
Computer=int(input("Enter the computer marks:"))

Percentage = (Physics +Chemistry+Biology+Mathematics+Computer) * 100/500

if(Percentage >= 90 ):
    print("Grade A")

elif(Percentage >=80):
    print("Grade B")

elif(Percentage >=70):
    print("Grade C")

elif(Percentage >=60):
    print("Grade D")

elif(Percentage >=40):
    print("Grade E")

else:
    print("Grade F")
