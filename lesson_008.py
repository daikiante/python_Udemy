# 辞書型

d = {'x':10,'y':20}

print(type(d))

print(d['x'])
print(d['y'])

d['x'] = 100
print(d['x'])


# 文字列も入る
d['x'] = 'XXX'
print(d['x'])



# キーとバリューの取り出し
print(d.keys())
print(d.values())


# d.update(d2) = dにd2の値をアップデート(オーバーライド=上書き)する
d2 = {'x':1000,'j':500}
d.update(d2)
print(d)


# .get(キー)  ==> 何も無い場合は'NoneType'が返ってくる
print(type(d.get('z')))

# .pop(キー)  ==> キーとバリューを取り除く
d.pop('x')
print(d)

# del キー  ==> キーとバリューを取り除く  ###(delだけだと定義そのものが消える)
del d['y']
print(d)

# .clear()  ==> 辞書を空にする  ###(定義した変数は残る)
d.clear()
print(d)


print('----------------')

d = {'x':10,'y':20}


# 'キー' in 辞書  ==> 辞書の中に'キー'があるか判定
print('x' in d)