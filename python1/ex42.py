# Animal é-um object (Sim, é meio confuso), veja o criterio extra

class Animal(object):
    pass

# Dog é-uma instancia de Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog tem-um atributo chamado name
        self.name = name
        print(self.name)

# Cat é-uma instancia de Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat tem um atributo chamado name
        self.name = name
        print(self.name)

# Person é-um objeto
class Person(object):

    def __init__(self, name):
        ##?? Person tem-um atributo chamado name
        self.name = name
        print(self.name)

        ## Person tem-um atributo pet
        self.pet = None
        print(self.pet)


# Employee é-uma instancia de Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm, o que é essa mágica estranha?
        super(Employee, self).__init__(name)
        ## Employee tem um atributo chamado salary
        self.salary = salary
        print(self.salary)

# Fish, salmon e halibut são objetos
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover é-um Dog

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

flipper = Fish()

crouse = Salmon()

harry = Halibut()
