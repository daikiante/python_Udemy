s = 'My name is Mike. Hi Mike.'
print(s)

is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('aaaaa')
print(is_start)

print('----------------------------')


# 文字列'Mike'がどこにあるか調べる rをつけると後ろから
print(s.find('Mike'))

print(s.rfind('Mike'))

# 何個含んでいるか調べる　　count()
print(s.count('Mike'))

# capitalize = 初めを大文字  title = 単語毎に大文字
# upper = 全て大文字  lower = 全てを小文字
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())

# replace(○○を××に置き換える)
print(s.replace('Mike','Nancy'))