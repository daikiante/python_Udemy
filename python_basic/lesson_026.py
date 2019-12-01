# ファイルの作成


# 上書きする特性がある
f = open('text.txt','w')
f.write('Text\n')
print('My','name','is','Mike', sep='#', end='!', file=f)
f.close()


# withステートメントでファイルをオープンする
# ファイルを勝手に閉じてくれるのでf.closeが不要
with open('text.txt','a') as f:
    f.write('\ntext')


# ファイルの読み込み
s = '''\
AAA
BBB
CCC
DDD
'''

with open('text.txt', 'w') as f:
    f.write(s)

# ファイルの読み込み
# with open('text.txt', 'r') as f:
#     # print(f.read())
#     while True:
#         line = f.readline
#         print(line)
#         if not line:
#             break


# with open('text.txt', 'r') as f:
#     # print(f.read())
#     while True:
#         chunk = 2
#         line = f.read(chunk)
#         print(line)
#         if not line:
#             break



# seekを使って移動する
# with open('text.txt', 'r') as f:
#     print(f.tell())
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))
#     f.seek(14)
#     print(f.read(1))
#     f.seek(15)
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))



# 書き込み読み込みモード
# w+で'書き込み+読み込み'という意味になる
# sesk(0)で読み込む位置を指定してあげる

with open('text.txt', 'w+') as f:
    f.write(s)
    f.seek(0)
    print(f.read())


# 読み込み書き込みモード
# r+で'読み込み+書き込み'という意味になる
# sesk(0)で書き込む位置を指定してあげる

with open('text.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)