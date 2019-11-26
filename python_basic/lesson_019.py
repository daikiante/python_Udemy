'''

sorte
並び替えをしてくれる関数

reverse = True とすることで反対から並び替えてくれる

'''


ranking = {
    'A':100,
    'B':85,
    'C':95
}

print(sorted(ranking, key = ranking.get, reverse = True))

print('--------------------')










# default dictionary
# 辞書の中に指定した文字が何個あるか調べる

s = 'kafjdlkfjdlkghjfhalkfjalksjaksjdgaksdjadlkjfa'

d = {}

for c in s:
    if c not in d:
        d[c] = 0
    
    d[c] += 1

print(d)

print('--------------------')


# setdefaultを定義することで何もないkeyには0と返してくれる
d = {}

for c in s:
    d.setdefault(c, 0)
    
    d[c] += 1

print(d)

print('--------------------')


# collectionsからdefaultdictを読み込んで上げることでsetdefaultを毎回定義する手間が省ける
from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)


print(d['e'])