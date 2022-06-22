amount=int(input("enter amount"))
if amount>=5:
  a=amount//2000
  b=amount%2000
  c=b//500
  d=b%500
  e=d//20
  f=d%200
  g=f//50
  print("notes of 2000=a,""notes of 500=c,""notes of 200=e,""notes of 50=g,")
else:
  print("not amount")

