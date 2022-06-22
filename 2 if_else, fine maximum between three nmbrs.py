a=input("enter num")
b=input("enter num")
c=input("enter num")
if a>b and a>c:
    print("a is max")
elif a<b and c<b:
    print("b is max")
elif a<c and b<c:
    print("c is max")
else:
    print("not max")
