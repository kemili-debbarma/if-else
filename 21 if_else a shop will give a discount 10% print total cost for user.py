unit=int(input("enter num"))
quantity=unit*10
if quantity>100:
   discount=quantity*10/100
   total_cost=quantity-discount
   print("total_cost=",total_cost)
else:
   print("not quantity")


