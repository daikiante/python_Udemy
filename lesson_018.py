# ジェネレーター

l = ['Good morning','Good afternoon','Good night']

for i in l:
    print(i)


print('----------------')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)

# yieldは繰り返し処理を一度抜ける性質がある
g = greeting()
print(next(g))
print('--------ここが間の処理--------')
print(next(g))
print('----------------')
print(next(g))
print('----------------')






# リスト内包表記

t = (1,2,3,4,5)

r = []
for i in t:
    r.append(i)

print(r)

# 1行で書ける
# appendを使わないので早い
r = [i for i in t]
print(r)



# 辞書 包括表記
w = ['mon','tue','wed']
f = ['coffee','milk','water']

d = {}
for x,y in zip(w, f):
    d[x] = y

print(d)


# 1行で書ける
d = {x: y for x, y in zip(w, f)}
print(d)


# ジェネレーター内包表記

def g():
    for i in range(10):
        yield i

g = g()

g = (i for i in range(10))

for x in g:
    print(x)


print('--------------------------')



'''
名前空間とスコープ

defの中(local)ではanimalが宣言されていないので、1行目のanimalは宣言していない変数を
呼び出そうとしているためエラーになる。

'''
animal = 'cat'

def f():
    # print(animal)
    animal = 'dog'
    print('after:',animal)

f()
print('global:',animal)


print('--------------------------')







'''
例外処理

本来ならリストlにインデックス5はない。
try,exceptを使うことでエラーを抜けて
Don't worryが実行される。
'''

l = [1,2,3]
i = 5

try:
    l[i]
except:
    print("Don't worry!")

# exceptが何も実行されなかった場合のみ実行される
else:
    print('done')

# finallyは必ず実行される
finally:
    print('clean up')






print('--------------------------')




'''
独自例外処理

間違っていたとしても、
次の処理に進んでくれる。
'''

class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE','orange','banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault, Go next')