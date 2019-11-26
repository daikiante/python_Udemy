# リストのメソッド

r = [1,2,3,4,5,1,2,3]


# r.index(探してるもの) = '探してるもの'はどのインデックスか可視化
print(r.index(3))

# この場合3番目のインデックスから2を探してください　という意味
print(r.index(3,2))


# このリストの中に5はありますか？
if 5 in r:
    print('あります')


# r.sort() = 文字を近い順に並べ替えてくれる
r.sort()
print(r)

# r.sort() = 逆から並べ替えてくれる
r.sort(reverse=True)
print(r)

# r.sort() = 逆から並べ替えてくれる
r.reverse()
print(r)



# s.split('文字を指定') = 指定した文字で区切り、リストに入れる
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)


# x = '文字を指定'.join(to_split) = 指定した文字でまとめてくれる
x = ' '.join(to_split)
print(x)

x = '###'.join(to_split)
print(x)


'''

print(help(list))
リストのメソッドを表示してくれる

'''