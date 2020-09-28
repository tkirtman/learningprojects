def collatz(number):
    if int(number) % 2 == 0:
        global output
        output = (int(number) // 2)
        #print(int(number) // 2)
    else:
        output = (3 * int(number) + 1)
        #print( output )

while True:
    turns = 0
    output = 0
    print ('Collatz a number:')
    number = input ()
    list = []
    while output !=1:
        collatz(number)
        list = list + [output]
        number = output
        turns = turns + 1
    print('Max: ' )
    print('Distance: ' + str(turns) )
    print(list)
