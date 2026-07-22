units = int(input("Enter electricity bill:"))
if units <=100:
    bill_amount = units*2
elif units <=200:
      bill_amount=200 + (units-100)*3

elif units <=300:
      bill_amount=200 + 300 + (units-200)*5

else:
    bill_amount=200 + 300 + 500 +(units-300)*7

    print("bill amount is:",bill_amount)