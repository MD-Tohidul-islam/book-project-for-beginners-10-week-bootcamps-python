# number = 5
# def scopeTest():
#     number +=1
# scopeTest()

sports = ['baseball','football','hockey','basketball']
def change(aList):
    aList[0] = 'soccer'
print('before altering: {}'.format(sports))
change(sports)
print(f'after altering: {sports}')