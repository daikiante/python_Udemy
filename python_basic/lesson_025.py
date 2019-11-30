class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self.word):
        return self.text.lower() + self.text.lower()

w = Word('text')

w2 = Word('##########')

w.text + w2.text

print(w + w2)
