# 配列

n = [1,2,3,4,5,6,7,8,9,10]

# n.appne() = 最後に追加
# n.insert(インデックスナンバー, ) = 最初に追加
# n.pop() = 後ろから取り除く

n.append(100)
print(n)

n.insert(0,200)
print(n)

n.pop()
print(n)



# del n[インデックスナンバー] = 消す
# del n = nの存在自体を消す

del n[0]
print(n)



# remove(消したいもの) = 消す。無いとバリューエラーになる

n.remove(2)
print(n)



# リストの結合 - 1
a = [1,2,3,4,5]
b = [6,7,8,9,10]
x = a + b
print(x)

a += b
print(a)



# ここからa b x n 全て消す
del a
del b
del n
del x

print('--------------------------------')



# リストの結合 - 2
x = [1,2,3,4,5]
y = [6,7,8,9,10]


# x.extend(足したいもの) = リストの結合  ※リストでしか使えない
x.extend(y)
print(x)

