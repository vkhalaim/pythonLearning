class Animal(object):
    def __init__(self, species, type):
        self.species = species
        self.type = type


class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_dangerous(self, animal):
        return animal.type in ['predator', 'toxic']


dog = Animal('dog', 'mammal')
wolf = Animal('wolf', 'predator')
cat = Animal('cat', 'predator')
snake = Animal('snake', 'toxic')

man = Human('Tom', 22)
print(man.is_dangerous(dog))
print(man.is_dangerous(wolf))
print(man.is_dangerous(cat))
print(man.is_dangerous(snake))
