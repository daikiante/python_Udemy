# オブジェクト指向

class Person(object):
    def __init__(self, age = 1):
        self.age = age

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No Drive')

class Baby(Person):
    def __init__(self, age = 1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age = 18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model = None):
        self.model = model

    def ride(self, person):
        person.drive()


car = Car()
# car.ride(baby)
car.ride(adult)