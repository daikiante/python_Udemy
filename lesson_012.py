# in  not

y = [1,2,3]
x = 1

if x in y:
    print('in')


if 100 not in y:
    print('not in')




# Pythonicな書き方

a = 1
b = 2

if not a == b:
    print('Not equal')

# 同じ式が論理演算子で書ける

if a != b:
    print('Not equal')






# 値が入っていないときのテクニック(Tips)

is_ok = True

if is_ok:
    print('OK!')
else:
    print('No!')


# 0の場合はFalse  1以上の場合はTrue  ''空の文字列はFalse  何か入っていればTrue
# False   0, 0.0, '', [], {}, set()

is_ok = 0

if is_ok:
    print('OK!')
else:
    print('No!')






# Noneを表示する
# Pythonでは空の状態をNoneとする

is_empty = None
# print(help(is_empty))


# == は is で表現することもできる
if is_empty is None:
    print('None!!')


# isは"オブジェクトが同じかどうか"判定する

print(1 == True)
print(1 is True)