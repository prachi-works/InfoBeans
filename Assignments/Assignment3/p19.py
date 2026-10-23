# 19. Write a program to input choice from user. If user enter ‘+’ as choice then calculate addition of 2 number. If Choice ‘>’ then check which number is greaterst. If choice is ‘==’ then check both number is equal or not.
choice = input("Enter your choice (+, >, ==): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '+':
    result = num1 + num2
    print("Addition:", result)

elif choice == '>':
    if num1 > num2:
        print(num1, "is greater")
    elif num2 > num1:
        print(num2, "is greater")
    else:
        print("Both numbers are equal")

elif choice == '==':
    if num1 == num2:
        print("Both numbers are equal")
    else:
        print("Both numbers are not equal")

else:
    print("Invalid choice")