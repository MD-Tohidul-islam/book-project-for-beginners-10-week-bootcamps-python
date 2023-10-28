class Dog():
    name = ''

    def setname(self,new_name):
        self.name = new_name

    def getname(self):
        return self.name
    def __str__(self):
        return 'this is a dog class'
sam = Dog()
sam.setname('Sammi')
sam.getname()
print(sam.getname())
print(sam)

class Animals():
    species = ''
    def setspecies(self,new_species):
        self.species = new_species
    def get_species(self):
        return self.species
lion = Animals()
lion.setspecies('feline')
lion.get_species()
print(lion.get_species())