## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-a
class Dog(Animal):
    def __init__(self, name):
        ## has-a
        self.name = name
## is-a
class Cat(Animal):
    def __init__(self, name):
         ## has-a
         self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## run the __init__ method of a parent class reliably - inheritent
        ## super(Employee, self).__init__(name) - for Python 2
        super().__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary's pet is satan
mary.pet = satan

## frank is-a Employee, his salary is 120000
frank = Employee("Frank", 120000)
print(frank.name, frank.salary, frank.pet)

## frank's pet is rover
frank.pet = rover
print(frank.name, frank.salary, frank.pet.name)

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
