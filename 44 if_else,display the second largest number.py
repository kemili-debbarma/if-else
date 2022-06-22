a=int(input("enter n um"))
b=int(input("enter num"))
c=int(input("enter num"))
if a<b and a>c:
    print("a is second largest") 
elif a>b and b>c:
    print("b is second largest")
elif a<c and b>c:
    print("c is second largest")
else:
    print("no second largest")
