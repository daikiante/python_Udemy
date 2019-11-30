# プロパティーを使った属性の変更
# エラーになっていたら成功 => 書き換えたくない関数を@propertyで守っているため

# class Car(object):
#     def __init__(self, model = None):
#         self.model = model

#     def run(self):
#         print('run')

# class TeslaCar(Car):
#     def __init__(self, model = 'Model S', enable_auto_run = False):
#         # super()は親の__init__を呼び出す
#         super().__init__(model)
#         self._enable_auto_run = enable_auto_run

#     @property
#     def enable_auto_run(self):
#         return self._enable_auto_run

# エラーになるので試すときだけコメント解除
# tesla_car = TeslaCar('Model S')
# tesla_car.enable_auto_run = True
# print(tesla_car.enable_auto_run)



# 書き換えるには？ => @関数名.setter を使う


class Car(object):
    def __init__(self, model = None):
        self.model = model

    def run(self):
        print('run')

class TeslaCar(Car):
    def __init__(self, model = 'Model S', enable_auto_run = False):
        # super()は親の__init__を呼び出す
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable

tesla_car = TeslaCar('Model S')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
