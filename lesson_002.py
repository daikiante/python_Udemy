# helpコマンド　　関数、ライブラリの機能が表示される

# import math

# print(help(math))


# ''  ""  \n ==> 改行
print('say "I don\'t know"')

print('hello \n how are you')





# インデックスとスライス

word = 'Python'

print(word[0])

print(word[1])

print(word[-1])

print(word[0:2])

print(word[2:5])

print('----------------------------')

'''
インデックスの更新

Python ==> Jython

word[0] = 'J'  だとエラーになる

word = 'J' + word[1:]   <===これで解決

'''

word = 'J' + word[1:]
print(word)


# インデックスの長さ　len()
n = len(word)
print(n)