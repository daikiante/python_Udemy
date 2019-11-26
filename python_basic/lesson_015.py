'''

関数定義


def say_something():
    print('hi')

say_something()

f = say_something()

'''

# retun

def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)


# 関数の中のif

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


r = what_is_this('red')
print(r)


# 関数の引数 ==> デフォルト引数を設定することもでき、上書き可能

def menu(entree,drink,dessert='lassi'):
    print('entree =',entree)
    print('drink =',drink)
    print('dessert =',dessert)

menu(entree='beef',drink='beer',dessert='ice')







# 空のリストに引数を使って要素を追加する
# Pythonでは関数で空のリストを作ることはタブー。理由は参照渡しになってしまうため。
# なのでNoneとおく

def test_func(x,l=None):
    if l is None:
        l = []
    l.append(x)
    return l

# # リスト'y'を生成して追加する
# y = [1,2,3]
# r = test_func(100,y)
# print(r)

r = test_func(100)
print(r)




# return

def add_list(a,b,c):
    return a * b * c

result = add_list(2,3,4)
print(result)
