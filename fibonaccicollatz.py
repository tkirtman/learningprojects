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
print('How far in the Fibonacci sequence would you like to go?', end=' ')
fibDistance = int(input())
ofibdist=fibDistance
while int(fibDistance) > 0:
    y=x+z # 1,1,0
    flist = flist + [y]
    fibDistance = fibDistance - 1
    if fibDistance == 0:
        break
    z=x+y # 2,1,1
    flist = flist + [z]
    fibDistance = fibDistance - 1
    if fibDistance == 0:
        break
    x=y+z # 3,2,1
    flist = flist + [x]
    fibDistance = fibDistance - 1
    if fibDistance == 0:
        break

for i in range(int(ofibdist)):
    turns = 0
    output = 0
    number = flist[i]
    while output !=1:
        collatz(number)
        number = output
        turns = turns + 1
    distance = int(turns)
    cList = cList + [distance]
    
print('Fibonacci sequence: ', end=' ') 
print(flist)
print('Collatz distances:  ', end=' ')
print(cList)
