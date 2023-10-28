#  creating a basic iterator from iterable

sports = ['baseball','soccer','football','hockey','basketball']
my_iter = iter(sports)
print(next(my_iter))  # outputs first item
print(next(my_iter))  # outputs 2nd item
for item in my_iter:
    print(item)
#print(next(my_iter))  # will produce error

#  creating our own iterator
class Alphabet():
    def __iter__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.index = 0
        return self
    def __next__(self):
        if self.index <= 25:
            char = self.letters[self.index]
            self.index+=1
            return char
        else:
            raise StopIteration
for char in Alphabet():
    print(char)
#  creating our own range generator with start,stop, and step
def myRange(stop,start = 0, step =1):
    while start < stop:
        print('generator start Value: {}'.format(start))
        yield start
        start +=step
for x in myRange(5):
    print('For loop x value:{}'.format(x))
    



