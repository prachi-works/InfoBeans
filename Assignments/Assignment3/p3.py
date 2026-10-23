# 3.A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("Enter the salary:"))
year_of_service=int(input("Enter the year of service :"))

if(year_of_service > 5):
    bonus=salary * 5 /100
else:
    bonus = 0
print("Net Bonus :",bonus)