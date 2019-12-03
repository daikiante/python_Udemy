# tarfileの圧縮展開


# lesson_030フォルダを .tar.gzに圧縮する

import tarfile

# with tarfile.open('test.tar.gz', 'w:gz') as tr: 
    # tr.add('/Users/daikiyamada/Documents/Projects/python_udemy/python_basic/lesson_030')


# # tarfileをPythonの中で展開する
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     tr.extractall(path='test_tar')


# 解凍せずに中身をみる
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('python_basic/test_tar/Users/daikiyamada/Documents/Projects/python_udemy/python_basic/lesson_030/test.txt') as f:
        print(f.read())