import time
def collatz(number):
    if int(number) % 2 == 0:
        global output
        output = (int(number) // 2)
        print(int(number) // 2)
    else:
        output = (3 * int(number) + 1)
        print( output )
while True:
    output = 0
    print ('Collatz a number:')
    number = input ()
    list = [int(number)]
    while output !=1:
        collatz(number)
        list = list + [output]
        number = output
        time.sleep(0.1)
    print('You win.')
#    print(list)
