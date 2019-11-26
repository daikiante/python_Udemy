# 位置引数のタプル化

'''
基本形はこれ

def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi','Mike','Nancy')

'''

# 最初のwordは第一引数、その他は*argsにまとめられる
# *argsは受け取った引数をまとめてtuple化してくれる

def say_something(*args):
    for arg in args:
        print(arg)

t = ('Mike','Nancy')
say_something('Hi',*t)



print('-----------------------')



# キーワード引数の辞書化
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree':'beef',
    'drink':'ice coffee',
    'dessert':'ice'
}

menu(**d)





print('-----------------------')




# 位置引数のタプル化とキーワード引数の辞書化

def menu(food, *args, **keyargs):
    print(food)
    print(args)
    print(keyargs)

# banana=food  
# apple,orange=*args  
# entree='beef',drink='coffee'=**keyargs
menu('banana','apple','orange', entree='beef', drink='coffee')
