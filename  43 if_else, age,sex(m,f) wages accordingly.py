age=int(input("enter num"))
sex=input("enter sex")
day=int(input("enter day"))
if age>=18 and age<=30 and sex=="m":
    wage=day*700
    print("wage",wage)

elif age>=18 and age<=30 and sex=="f":
    wage=day*750
    print("wage",wage)
elif age>=30 and age<=40 and sex=="m":
    wage=day*800
    print("wage",wage)
elif age>=30 and age<=40 and sex=="f":
    wage=day*850
    print("wage",wage)
else:
    print("non")
