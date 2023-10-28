class Dog():
    sound = 'bark'
    def makesound(self):
        print(self.sound)
    def printInfo():
        print('i am a dog')
Dog.printInfo()
print(Dog.sound)
#Dog.makesound() this make erro
sam = Dog()
print(sam.sound)
#sam.printInfo() this make erro
sam.makesound()