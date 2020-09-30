def collatz(number):
    if int(number) % 2 == 0:
        global output
        output = (int(number) // 2)
        #print(int(number) // 2)
    else:
        output = (3 * int(number) + 1)
        #print( output )

x=1
z=0
flist = []
cList = []
# while x < 100:
print('How far in the Fibonacci sequence would you like to go?')
fibDistance = input()
for i in range (int(fibDistance)):
    y=x+z # 1,1,0
    print(y)
    flist = flist + [y]
    z=x+y # 2,1,1
    print(z)
    flist = flist + [z]
    x=y+z # 3,2,1
    print(x)
    flist = flist + [x]
print(flist)

for i in range(int(fibDistance)*3):
    turns = 0
    output = 0
    number = flist[i]
    while output !=1:
        collatz(number)
        number = output
        turns = turns + 1
    distance = str(turns)
    cList = cList + [distance]
    print(cList)
