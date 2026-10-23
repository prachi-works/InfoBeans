'''2.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user'''

quantity=int(input("Enter the Quantity"))
price=100

total_cost=price * quantity

if(total_cost > 1000):
    discount= total_cost * 10 /100
    final_cost=total_cost - discount
else:
    discount=0
    final_cost=total_cost*discount

print("Total Cost :",total_cost)
print("Discount : ",discount)
print("Final Cost :",final_cost)