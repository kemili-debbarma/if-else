unit=int(input("enter unit"))
if unit>=1 and unit<=50:
   a=unit*0.50+20/100
   print("bill=",a)
elif unit>50 and unit<151:
   a=unit*0.75+20/100
   print("bill=",a)
elif unit>151 and unit<=251:
   a=unit*1.20+20/100
   print("bill=",a)
elif unit>250:
   a=unit*1.50+20/100
   print("bill=",a)
else:
   print("none")

