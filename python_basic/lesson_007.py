# タプル型

t = (1,2,3,4,1,2)

print(type(t))


# 書き換え不可　(新しい値をアサインできない)
# 値を書き換えたく無い時、読み込み専用で使われるケースが多い
# タプル内にリストを追加することはできる！書き換えも可能！
# index slice はできる

t = 1
print(type(t))
# int

t = 1 ,
print(type(t))
# tuple    ==>  , が入るとタプル型として認識する




# タプルのアンパッキング

num_tuple = (10, 2)
print(num_tuple)

x , y = num_tuple
print(x,y)

print(type(x))
# int



# 値の入れ替え
a = 100
b = 200
print(a,b)

a,b = b,a
print(a,b)