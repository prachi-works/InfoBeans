# 47) WAP to print tables of all the numbers between two entered numbers

start=int(input('enter start  the number:'))
end=int(input('enter the end number:'))
print(f"\n----Multiplication Table from {start} to {end}----\n")

for num in range(start,end+1):
    print(f"Table of {num}:")

    #inner loop for table
    for i in range(1,11):
        product=num * i
        print(f"{num} *{i} = {product}")
    print("-"*15)

