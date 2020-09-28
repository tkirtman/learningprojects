def collatz(number):
    if int(number) % 2 == 0:
        global output
        output = (int(number) // 2)
        #print(int(number) // 2)
    else:
        output = (3 * int(number) + 1)
        #print( output )

#while True:
 #   turns = 0
  #  output = 0
   # #print ('Collatz a number:')
    #number = x
    #list = []
    #while output !=1:
     #   collatz(number)
      #  list = list + [output]
       # number = output
        #turns = turns + 1
    #print('Max: ' )
    #print('Distance: ' + str(turns) )
    #print(list)


x=1
z=0
oList = []
while x < 100:
    y=x+z # 1,1,0
    collatz(y)
    oList = oList + [output]
    #print(y)
    z=x+y # 2,1,1
    collatz(z)
    oList = oList + [output]
    #print(z)
    x=y+z # 3,2,1
    collatz(x)
    oList = oList + [output]
    #print(x)
print(oList)
