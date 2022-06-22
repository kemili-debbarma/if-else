month=input("enter month")
a=("january""murch""may""july""august""october""december")
b=("april""june""september""november")
if month in(a):
   print("31 day")
elif month in(b):
   print("30 day")
else:
   print("28 day")