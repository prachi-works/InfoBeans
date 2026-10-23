#Employee DAta

employee=(101,'Amit','It',40000)
print('Employee Id:',employee[0])
print('Employee name:',employee[1])
print('Employee Department:',employee[2])
print('Employee Salary:',employee[3])

# 2. Product Billing System
pname=input('enter product name:')
price=float(input('enter product price:'))
qty=int(input( 'enter the quantity'))

bill=(pname,price,qty)
total= bill[1] * bill[2]

print('Bill amount')
print('product name',bill[0])
print('total',total)
