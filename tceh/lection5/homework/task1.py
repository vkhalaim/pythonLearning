class Person(object):
    known_persons = []

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def know(self, person):
        if person not in self.known_persons:
            self.known_persons.append(person)
        else:
            print('I already know ', person.name)

    def is_known(self, person):
        if person in self.known_persons:
            print('I know this guy!')
        else:
            print('Who is this stranger?')


a = Person("a", 12)
b = Person("b", 12)
c = Person("c", 12)

a.know(b)
b.know(a)
a.is_known(b)
a.is_known(c)
