#  creating and applying our own decorator using the @ symbol
def decorator(func):
    def wrap():
        print('====')
        func()
        print('=====')
    return wrap


@decorator
def printName():
    print('john!')


print(printName())
#  Decorators with Parameters
def run_times(num):
    def wrap(func):
        for i in range(num):
            func()
    return wrap
@run_times(4)
def sayHello():
    print('Hello!')
# # Functions with Decorators and parameters
#  creating  a decorator for a function that accepts parameters
def birthday(func):
    def wrap(name,age):
        func(name,age+1)
    return wrap
@birthday
def celebrate(name,age):
    print(f'Happy birthday {name} you are now {age}')
print(celebrate('arpon' ,25))
# # Restricting Function Access
# real world sim, restricting function access
def login_required(func):
    def wrap(user):
        password = input('What is the password?')
        if password == user['password']:
            func(user)
        else:
            print('Access Denied')
    return wrap
@login_required
def restrictedfunc(user):
    print('Access granted, welcome {}'.format(user['name']))
user = {'name': 'tohidul','password':'1234'}
print(restrictedfunc(user))




