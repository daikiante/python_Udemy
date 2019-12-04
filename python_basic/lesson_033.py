# subprocess
# Pythonからターミナルを操作できる

import subprocess

# subprocess.run(['ls','-al'])

# 結果は一緒
# subprocess.run('ls -al', shell=True)


# datetime
import datetime

now = datetime.datetime.now()

print(now)

# 国際基準の時刻表示
print(now.isoformat())

# カスタマイズして表示する(西暦を4桁で表示したい場合はY)(%fはマイクロセカンド)
print(now.strftime('%d/%m/%y-%H%M%S%f'))

today = datetime.date.today()

print(today)
print(today.isoformat())
print(today.strftime('%d/%m/%y'))
print(today.strftime('%Y年 %m月 %d日'))



t = datetime.time(hour=1, minute=10, second=5, microsecond=100)

print(t)
print(t.isoformat())
print(t.strftime('%H%M%S%f'))


print('----------------')


# 過去の時間を扱いたい時
print(now)
d = datetime.timedelta(weeks=-1)
print(now + d)

# 結果は一緒
d = datetime.timedelta(weeks=+1)
print(now - d)



# time sleep
import time

# 3秒後に実行される
print('#########')
time.sleep(3)
print('#########')



'''

# 応用編
import os
import shutil

file_name = 'test.txt'

# test.txtがない場合、作る
if os.path.exists(file_name):
    shutil.copy(file_name, '{}.{}'.format(
        file_name, now.strftime('%y_%d_%m_%H_%M_%S')))

# バックアップを作る
with open(file_name, 'w') as f:
    f.write('test')

'''