a=int(input("a = "))
b=int(input("b = "))
yigindi=0
vvv=1
for son in range(a,b+1,1):
    yigindi=yigindi+a
    vvv*=yigindi
else:
    print(vvv)