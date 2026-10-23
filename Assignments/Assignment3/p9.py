# 9. Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

ch=input("Enter the character :")
if ch.isupper():
    print("Upper Case")
elif ch.islower():
    print("Lower Case")
else:
    print("it is not an alphabet")