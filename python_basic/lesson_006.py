# リストのコピー

i = [1,2,3,4,5]
j = i
print('i =', i)
print('j =', j)

'''

i = [1, 2, 3, 4, 5]
j = [1, 2, 3, 4, 5]

'''

# j = i なので、jを変えるとiも変わってしまう
i = [1,2,3,4,5]
j = i
j[0] = 100
print('i =', i)
print('j =', j)


print('-------------------')

# ではどうやって解決するか    答えは.copy()
x = [1,2,3,4,5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

'''

# リストの使い方
# 5人乗りのタクシーの場合

>>> seat = []
>>> min = 0
>>> max = 5
>>> min <= len(seat) < max     判定

seat.append('person')
seat.append('person')
seat.append('person')
seat.append('person')
seat.append('person')
# 暫定5人

seat.pop(0)
# 暫定4人

'''