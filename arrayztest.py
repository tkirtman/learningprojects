namedb = ['tkirtman', 'turdburg']
passdb = ['1234', '5678']

username = ()
password = ()

while username not in namedb:
    print('Username:')
    username = input()
    if username in namedb:
        print('Password:')
        password = input()

    else:
        print('Username not found.')
for attempts in range(3):
    if attempts == 2:
        print('Login Failed')
        print('Account Locked')
        break
    elif username == namedb[0] and password != passdb[0]:
        print('Incorrect password.')
        print('Enter password:')
        password = input()
    elif username == namedb[1] and password != passdb[1]:
        print('Incorrect password.')
        print('Enter password:')
        password = input()
    else:
        print('Success')
        break






















#Ask for a username
#ask for and save username

#Ask for the password to that username
#ask for and save password

#Check to see if password matches username
#check if username exists
#check if password matches username

#Print login success for fail


