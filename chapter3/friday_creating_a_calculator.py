# step 1 : ask user for calculation to be performed
operation = input('would you like to add/substract/multiply/divide?').lower()
print(f'you chose {operation}')
try:
    if operation == 'add':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'{x} + {y} = ',x+y)
    elif operation == 'subtraction':
        print('please keep in mind that the order of your numbers matter')
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'{x} - {y} = ', x - y)
    elif operation == 'multiply':
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        print(f'{x} * {y} = ', x * y)
    elif operation == 'divide':
        print('please keep in mind that the order of your numbers matter')
        x = float(input('Enter the first number: '))
        y = float(input('Enter the second number: '))
        try:
            print(f'{x} / {y} = ', x / y)
        except ZeroDivisionError:
            print('you can not divide any number by zero')
    else:
        print('you input wring operation')
except:
    print('Error : improper numbers used.please try again')
