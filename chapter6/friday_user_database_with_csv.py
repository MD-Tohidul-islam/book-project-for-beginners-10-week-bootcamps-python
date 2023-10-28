import csv
from IPython.display import clear_output
# handle user registration and writing to csv

def registerUser():
    with open('users.csv','a',newline = '') as f:
        writer = csv.writer(f,delimiter = ',')
        print('To register, please enter your info: ')
        email = input('E-mail: ')
        password = input('Password: ')
        password2 = input('Re-type password: ')
        clear_output()
        if password == password2:
            writer.writerow([email,password])
            print('You are now registered!')
        else:
            print('Something went wrong, Try again.')

#  ask for user info and return true to login or false if incorrect info
def loginuser():

    print('To login, please enter your info: ')
    email = input('E - mail: ')
    password = input('Password: ')
    clear_output()
    with open('users.csv',mode = 'r+') as f:
        reader = csv.reader(f,delimiter = ',')
        for row in reader:
            if row == [email,password]:
                print('you are now logged in!')
                return True
            print('Please register first\n Or Something went wrong , try again')
            return False
#  variable for main loop
active = True
logged_in = False
while active:

    if logged_in:
        print('1. Logout\n2. Quit')
    else:
        print('1. Login\n2. Register\n3.Quit')
    choice = input('What would you like to do? ').lower()
    clear_output()
    if choice == 'register' and logged_in == False:
        registerUser()
    elif choice == 'login' and logged_in == False:
        logged_in = loginuser()


    elif choice == 'quit':
        active = False
    elif choice == 'logout' and logged_in == True:
        logged_in = False
        print('you are now logged out.')
    else:
        print('Sorry, please try again!')


