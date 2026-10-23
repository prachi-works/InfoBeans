# 13. Write a  program that keeps a number from the user and generates an integer between 1 and 7 and displays the name of the weekday.
# Test Data
# Input number: 3
# Expected Output :
# Wednesday

day=int(input("Enter the day no."))

if day ==1:
    print("Monday")

elif day == 2:
    print("Tuesday")
elif day== 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day== 7:
    print("Sunday")
else:
    print("Invalid day")

