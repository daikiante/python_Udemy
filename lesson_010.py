# 集合型

a = {1,2,3,4,5,6,7,8,4,3,5,7,4,2,2}

# 重複しているものはまとめて表示される
print(a)
print(type(a))


# a - b = aにあるもの引くb  なので{1,2}  ===>6,7はaには無いので表示されない
a = {1,2,3,4,5}
b = {3,3,4,5,6,7}

print(a - b)


# a & b = aにもあってbにもあるもの  {3,4,5}
print(a & b)

# a | b = ab
print(a | b)

# a ^ b = aかbにはあるけど重複はしていないもの
print(a ^ b)


print('--------------------------')

# 集合型のメソッド
# 集合型にはインデックスの概念がない

s = {1,2,3,4,5}
print(s)


# .add(追加したい値) = 値を追加する
s.add(6)
print(s)

# .remove(消したい値) = 指定した値をを消す
s.remove(6)
print(s)

# .clear() = 値を空にする(定義そのものは消えない)
s.clear()
print(s)
# help(set)   ===>  メソッドが出る
print('-------------------------')



# 集合型の使い方
# 共通の知り合いを探すときなど

my_friends = {'A','B','C'}
A_friends = {'B','D','E'}

print(my_friends & A_friends)


# 買ったものの重複を探したいとき

fruits = ['apple','banana','apple','banana']

kind = set(fruits)

print(kind)