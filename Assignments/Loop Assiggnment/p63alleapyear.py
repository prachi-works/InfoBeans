# 61) WAP to find out all the leap years between two entered years

start = int(input("Enter the starting year: "))
end = int(input("Enter the ending year: "))

for year in range(start, end + 1):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(year)
