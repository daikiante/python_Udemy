# import文とAS


# 2通りのimport  (結果は一緒)

# import lesson_package.utils
# r = lesson_package.utils.say_twice('hello')
# print(r)


# from lesson_package import utils
# r = utils.say_twice('hello')
# print(r)



# 絶対パスと相対パスのimport
# 階層が増えたら.で繋ぐ

from lesson_package.talk import human

print(human.sing())

print(human.cry())


print('---------------')


from lesson_package.talk import *

print(animal.sing())

print(human.cry())