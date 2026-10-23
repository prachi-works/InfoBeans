# 15. Write a java program to accept the cost price of a bike
#     and display the road tax to be paid according to the 
#     following criteria.
#     Cost Price(In Rs)		Tax
#      > 100000			 15%
#      >50000 and <=100000	 10%
#      <=50000			 5%	

cost_price=int(input("Enter the cost price of bike"))

if cost_price > 100000:
    Tax= cost_price * 15 /100

elif cost_price > 50000 and cost_price <= 100000:
    Tax = cost_price * 10 / 100

else:
    Tax = cost_price * 5/100

print("Road Tax:",Tax,"Rs")