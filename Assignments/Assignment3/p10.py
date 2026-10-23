# 10.Write a program to check if a year is leap year or not.

year=int(input("Enter the year:"))

if(year % 100 == 0 and year % 400 == 0):
    print("Leap Year")
elif(year % 100 != 0 and year%4 == 0):
    print("Leap Year")
else:
    print("Normal Year")