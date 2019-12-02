# テンプレート

# import string

# s = """\
# Hi $name.

# $contents

# Have a good day
# """

# t = string.Template(s)
# contents = t.substitute(name='Mike', contents='How are you?')
# print(contents)


# テンプレート 実際に使う例

import string

with open('/Users/daikiyamada/Documents/Projects/python_udemy/python_basic/design/emal_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)
