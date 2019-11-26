# while文

count = 0

while count < 5:
    print(count)
    count += 1


print('-------------------')

# break = 終了(ループを抜ける)   continue = スキップ(次のループにいく)
count = 0

while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1


print('-------------------')


# while else   もしbreakで終了するとelseも抜ける =>　理由はbreakにループを抜ける性質があるから
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print('done')


    print('-------------------')


# input関数  ==> Trueの値を受け取るまで処理を続ける

while True:
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')


