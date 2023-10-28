def outputData(name,*args):
    print(type(args))
    for arg in args:
        print(arg)


outputData('john smith',5,True,'jess')

def outputData1(**kwargs):
    print(type(kwargs))
    print(kwargs['name'])
    print(kwargs['num'])
outputData1(name = 'john smith',num=5,b = True)


