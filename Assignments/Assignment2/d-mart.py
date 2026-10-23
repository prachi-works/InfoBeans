
n=input("enter the name of customer: ")
gender=input("enter the gender:")

item1=input("")
q1=int(input(""))
price1 = 10
total_price1=q1*price1
if q1>4:
  discount=(total_price1 * 5 )/100
else:
   discount =0
after_discount1=total_price1-discount



item2=input("")
q2=int(input(""))
price2 = 20
total_price2=q2*price2
after_discount2=total_price2


item3=input("")
q3=int(input(""))
price3=30
total_price3=q3*price3
after_discount3=total_price3


item4=input("")
q4=int(input(""))
price4=40
total_price4=q4*price4
after_discount4=total_price4

item5=input("")
q5=int(input(""))
price5=50
total_price5=q5*price5
discount=total_price5*10/100
After_discount5=total_price5-discount

item6=input("")
q6=int(input(""))
price6=60
total_price6=q6*price6
after_discount6=total_price6

item7=input("")
q7=int(input(""))
price7=70
total_price7=q7*price7
after_discount7=total_price7

item8=input("")
q8=int(input(""))
price8=80
total_price8=q8*price8
after_discount8=total_price8

item9=input("")
q9=int(input(""))
price9=90
total_price9=q9*price9
after_discount9=total_price9


item10=input("")
q10=int(input(""))
price10=100
total_price10=q10*price10
discount=total_price10 * 15/100
after_discount10=total_price10-discount

#account price and discount price
AP=(total_price1+total_price2+total_price3+total_price4+total_price5+total_price6+total_price7+total_price8+total_price9+total_price10)
DP=(after_discount1+after_discount2+after_discount3+after_discount4+After_discount5+after_discount6+after_discount7+after_discount8+after_discount9+after_discount10)

if DP > 10000:
   bill_discount= DP * 15 /100
elif DP>=5000 and DP <= 10000:
   bill_discount= DP * 10/100
else:
   bill_discount=0
bill_after_discount=DP-bill_discount
gst=bill_after_discount * 10 /100

carry_bag=input("Do you want an carry bag?(yes/no):")
if carry_bag.lower()=='yes':
   bag_amount = 10
else:
   bag_amount = 0

final_bill=bill_after_discount+gst+bag_amount

if gender.lower() == 'female':
   gift="Cadburry"
elif gender.lower()=='male':
   gift="Leather Wallet"
else:
   gift="No bag"



print("                                    D-Mart")
print(f"Name:{n}","                                                           Date:12/9/2022")
print("-------------------------------------------------------------------------------------------")
print("Item Name           Quantity            Price            Total               After ")
print(f"{item1}             {q1}            {price1}           {total_price1}Rs   {after_discount1} ")  
print(f"{item2}             {q2}            {price2}           {total_price2}Rs   {after_discount2} ")                                   

print(f"{item3}             {q3}            {price3}           {total_price3}Rs   {after_discount3}Rs ")
print(f"{item4}             {q4}            {price4}           {total_price4}Rs   {after_discount4}Rs ")
print(f"{item5}             {q5}            {price5}           {total_price5}Rs   {After_discount5}Rs ")
print(f"{item6}             {q6}            {price6}           {total_price6}Rs   {after_discount6}Rs ")
print(f"{item7}             {q7}            {price7}           {total_price7}Rs   {after_discount7}Rs ")
print(f"{item8}             {q8}            {price8}           {total_price8}Rs   {after_discount8}Rs ")
print(f"{item9}             {q9}            {price9}           {total_price9}Rs   {after_discount9}Rs ")
print(f"{item10}            {q10}           {price10}          {total_price10}Rs  {after_discount10}Rs ")

print("--------------------------------------------------------------------------------------------")
print( "                                                     A.P             D.P ")
print(f"                                                     {AP}            {DP}")
print(f"Gift :- {gift}                                       0.00            0.00")
print(f"\n\nCarry Bag:{carry_bag}                            {bag_amount}    {bag_amount}")
print(f"GST(10%)                                             {gst}          {gst}")
print("--------------------------------------------------------------------------------------------")
print(f"                                                     {final_bill}    {final_bill}")
print()
print("                                      Thank You")
print("                                        To Visit")
print("                                         D-Mart")


