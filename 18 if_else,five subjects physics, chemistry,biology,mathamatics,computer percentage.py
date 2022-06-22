a=int(input("enter percentage"))
b=int(input("enter percentage"))
c=int(input("enter percentage"))
d=int(input("enter percentage"))
e=int(input("enter percentage"))
percentage=(a+b+c+d+e)/500*100
if percentage>=90:
   print("grade a")
elif percentage>=80:
   print("grade b")
elif percentage>70:
   print("grade c")
elif percentage>=60:
   print("grade d")
elif percentage>40:
   print("grade e")
else:
   print("grade f")