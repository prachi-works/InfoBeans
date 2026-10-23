# Q3. Lists — Second-Largest Distinct Element (5 Marks)

# Given a list of integers, find the second-largest distinct element without using sort(), sorted(), or max().

# numbers = [12, 45, 7, 45, 30, 22, 30]

# Expected output: 30
numbers=[12,45,7,45,30,22,30]
s=set(numbers)

max=0
max2=0

for numbers in s:
    if numbers>max:
        max2=max
        max=numbers
    elif max2<numbers<max:
        max2=numbers
print(max2)     
