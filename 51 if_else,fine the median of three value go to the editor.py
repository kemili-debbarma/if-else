a=float(input("enter num"))
b=float(input("enter num"))
c=float(input("enter num"))
if a<b and b<c:
    print("b is median",b)
elif a>b and a<c:
    print("a is median",a)
elif a>c and b<c:
    print("c is median",c)
else:
    print("no median")