# ファイル操作

import os
import pathlib
import glob
import shutil

# text.txtはありますか True or False
print(os.path.exists('text.txt'))

# text.txtはファイルですか True or False
print(os.path.isfile('text.txt'))

# designというフォルダはありますか True or False
print(os.path.isdir('python_basic/design'))

# ファイルの名前変更 (変えたいファイル, 新しい名前)
# os.rename('text.txt', 'renamed.txt')

# renamed.txtとsymlink.txtをコピーしてリンクさせる
# os.symlink('python_basic/renamed.txt', 'python_basic/symlink.txt')

# フォルダを作る
# os.mkdir('test_dir')

# フォルダを消す (何も入っていないとき有効)
# os.rmdir('test_dir')

# 空のファイルを作る (impot pathlib が必要)
# pathlib.Path('empty.txt').touch()

# ファイルを削除する
# os.remove('empty.txt')

# フォルダの中にあるフォルダを表示する (lsコマンドと似てる)
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))

# 中身を全て表示 (*は全てという意味/import globが必要)
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()
print(glob.glob('test_dir/test_dir2/*'))

# ファイルをコピーする (import shutilが必要)
# shutil.copy('test_dir/test_dir2/empty.txt', 'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))

# フォルダを消す (中身が入っていても有効)
# shutil.rmtree('test_dir')

# カレントディレクトリを表示
print(os.getcwd())