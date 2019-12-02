# ファイル操作

import os

# text.txtはありますか True or False
print(os.path.exists('text.txt'))

# text.txtはファイルですか True or False
print(os.path.isfile('text.txt'))

# designというフォルダはありますか True or False
print(os.path.isdir('python_basic/design'))

# ファイルの名前変更 (変えたいファイル, 新しい名前)
# os.rename('text.txt', 'renamed.txt')

# renamed.txtとsymlink.txtをコピーしてリンクさせる
os.symlink('python_basic/renamed.txt', 'python_basic/symlink.txt')