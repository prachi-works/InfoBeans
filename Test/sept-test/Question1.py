
# Q1. Electricity Bill Calculator — if-elif-else

# Write a Python program to calculate the electricity bill based on the number of units consumed.

# Use the following slab rates:

# Units	Rate
# First 100 units	₹5/unit
# Next 100 units	₹7/unit
# Next 200 units	₹10/unit
# Above 400 units	₹12/unit

# The program should accept the number of units from the user and calculate the total bill.

# Example:

# Enter units: 350
# Electricity Bill: ₹2700

no_of_units=float(input('enter the no. of units'))

if no_of_units==100:
    first_hundred_units = 5 * 100 / no_of_units

elif no_of_units>100 and no_of_units<=200:
    next_hundred_units= 7 * 100 / no_of_units

elif no_of_units>200 and no_of_units<=400:
    next_twohundred_items= 10 * 100/ no_of_units
elif no_of_units>400:
    above_fourhundred_units= 12 * 100/no_of_units

total_bill=first_hundred_units + next_hundred_units + next_twohundred_items + above_fourhundred_units

print(f"The total bill of electricity is RS {total_bill}")