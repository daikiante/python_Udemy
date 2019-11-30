# クラスメソッドとスタティックメソッド

class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about():
        print('about human')

a = Person()
print(a.x)

# bのPersonは()がないのでオブジェクトとして宣言されていないがkindはPerson内のグローバル変数なので出力できる
# 逆にself.xにはアクセスできない
b = Person
print(b.kind)

print('---------------')

a = Person()
print(a.what_is_your_kind())

# @classmethod があることによって、まだオブジェクトじゃない状態でも「クラスのメソッドです」という意味になる
# つまり @classmethod があることによって、()が無くても呼び出すことができる
b = Person
print(b.what_is_your_kind())

print(Person.kind)
print(Person.what_is_your_kind())

print('---------------')

# @staticmethodは引数いらない
Person.about()