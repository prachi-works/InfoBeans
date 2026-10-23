# 12.A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895 

original_no=int(input("Enter the four digit no."))
print("Original no is ",original_no)

if (original_no>=1000 and original_no<=9999):
     d1=original_no % 10
     original_no= original_no // 10

     d2=original_no %10
     original_no = original_no // 10

     d3=original_no % 10
     original_no = original_no // 10

     d4=original_no % 10
     original_no = original_no // 10

     reversed_no=d1 *1000+ d2*100+d3*10 + d4
     print("Reversed no is :",reversed_no)
else:
     print("Please enter a 4 digit no.")