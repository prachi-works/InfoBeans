# 8. Calculate the sum of all numeric values in a dictionary.
d={
    '1':101,
    "str" :"hariom",
    'age':22,
    'marks':90
    }
result={}
sum=0
for key,value in d.items():
    
    if isinstance(value,(int,float)):
      sum=sum+value
print(sum)



    