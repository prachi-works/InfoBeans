# Q2. Simple Calculator — match-case

# Write a Python program that accepts:

# Two numbers
# An operator (+, -, *, /, %)

# Use match-case to perform the selected operation.

# The program should also handle division by zero.

# Example:

# Enter first number: 20
# Enter second number: 5
# Enter operator: /

# Result: 4.0

first_number=int(input('enter the first number:'))
second_number=int(input('enter the second number:'))

operator=input('enter the operator:')

match operator:
    case'+':
        print(f'Addition of number{first_number+second_number}')
    case'-':
        print(f'Subtraction of number{first_number-second_number}')
    case'*':
        print(f'Multiplication of number{first_number*second_number}')
    case'/':
        print(f'division of two number{first_number/second_number}')
    case'%':
        print(f'Modulation of two number{first_number% second_number}')  