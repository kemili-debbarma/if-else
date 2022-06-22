a=int(input("enter num"))
b=int(input("enter num"))
c=int(input("enter num"))
if a==b and c==a:
   print("it is equilateral")
elif a==b and c!=a:
    print("it is isosecles")
elif a!=b and c!=a:
    print("it is scalene")
else:
    print("no triangle")