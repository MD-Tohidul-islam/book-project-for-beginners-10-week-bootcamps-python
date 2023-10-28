#  using the super() method
class Animal():
    def __init__(self,species):
        self.species = species

class Dog(Animal):
    def __init__(self,species,name):
        self.name = name
        super().__init__(species)
sam = Dog('canine','sammi')
print(sam.species)
print(sam.name)
class Animal2():
    def maskesound(self):
        print('roar')
class Dog2(Animal2):
    def makesound(self):
        print('bark')
sam,lion = Dog2(),Animal2()
sam.makesound()
lion.maskesound()
#  inheriting multiple classes
class physics():
    gravity = 9.8

class Automobile():
    def __init__(self,make,model,year):
        self.make,self.model,self.year = make,model,year
class Ford(physics,Automobile):
    def __init__(self,model,year):
        Automobile.__init__(self,'ford',model,year)
truck = Ford('F-150',2018)
print(truck.gravity,truck.make,truck.model,truck.year)

