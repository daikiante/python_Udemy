# 制御フロー if


# if文は上から見て最初にTrueのものが処理される
x =  0
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('positive')



# 比較演算子

# aとbが等しい
# a == b

# aとbが異なる
# a != b

# aがbよりも小さい
# a < b

# aがbよりも大きい
# a > b

# aがb以下である
# a <= b

# aがb以上である
# a >= b

# aもbもTrueであればTrue
# a and b

# aまたはbがTrueであればTrue
# a or b