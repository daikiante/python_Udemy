# 関数内関数 (inner function)

def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(a, b)
    print(r1 + r2)


outer(1, 2)




print('-----------------------------')


# クロージャー

def outer(a, b):

    def inner():
        return a + b

    return inner

f = outer(1, 2)
r = f()
print(r)


print('-----------------------------')



# デコレーター

def print_info(func):
    def wrapper(*args, **keyargs,):
        print('start')
        result = func(*args, **keyargs,)
        print('end')
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)


print('-----------------------------')






# ラムダ

l = ['Mon','tue','Wed','Thu','fri','sat','Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# 本来なら２行で書いていたものが
# def sample_func(word):
#     return word.capitalize()

# ラムダを使うと１行になる
change_words(l, lambda word: word.capitalize())



print('-----------------------------')



