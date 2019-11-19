# 辞書型のコピー

x = {'a':1}
y = x
y['a'] = 1000

print(x)
print(y)

# x = {'a':1} = y なので、yを変えるとxも変わってしまう
# .copy() を使うと解決する(参照渡し)

x = {'a':1}
y = x.copy()

y['a'] = 1000

print(x)
print(y)







print('-'*25)

# 辞書の使い方

fruits = {
    'apple':100,
    'banana':200,
    'orange':300
}

print(fruits['apple'])

