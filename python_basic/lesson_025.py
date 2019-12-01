# 特殊メソッド

class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == self.text.lower()

# addメソッドを使うことで文字列同士を足すことができる (+をつけると呼び出される)
w = Word('this is test')
w2 = Word('##########')

print(w + w2)


print('-----------------')

# eq(イコール)メソッドを使うことで文字列同士が同じものかどうか判定してくれる(==をつけると呼び出される)
# w w2は中身は同じ文字だが違うオブジェクトなので__eq__を消して==で判別するとFalseになる

w = Word('test')
w2 = Word('test')

print(w == w2)


print('-----------------')
