x=1
z=0
while x < 100:
    y=x+z # 1,1,0
    print(y)
    z=x+y # 2,1,1
    print(z)
    x=y+z # 3,2,1
    print(x)

