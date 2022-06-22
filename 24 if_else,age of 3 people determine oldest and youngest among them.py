a=input("enter age")
b=input("enter age")
c=input("enter age")
if a>b and a>c:
   print("a is oldest")
elif a<b and c<b:
   print("b is oldest")
elif a<c and b<c:
   print("c is oldest")
else:
   print("no oldest")