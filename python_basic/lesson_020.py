# クラスの生成

class Person(object):
    def __init__(self, name):
        self.name = name
        
    def say_somethig(self):
        print(f'Im {self.name}. Hello')

person = Person('Daiki')
person.say_somethig()


# クラスの継承

class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()




# クラスのオーバーライド (再度定義すると上書きできる)
# superによる親メソッドの呼び出し


class Car(object):
    def __init__(self, model = None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class HondaCar(Car):
    def run(self):
        print('super run')

class TeslaCar(Car):
    def __init__(self, model = 'Model S', enable_auto_run = False):
        # super()は親の__init__を呼び出す
        super().__init__(model)
        self.enable_auto_run = enable_auto_run

    def run(self):
        print('super fast')
    
    def auto_run(self):
        print('auto run')


car = Car()
car.run()
print('------------')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('------------')
tesla_car = TeslaCar('Model S')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()

