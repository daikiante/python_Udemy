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


