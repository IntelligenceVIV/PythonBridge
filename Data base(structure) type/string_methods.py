# @Time    : 2019/4/18 4:40
# @Author  : Noah
# @File    : string_methods.py
# @Software: PyCharm
# @description: string methods
from pprint import pprint

string = "Because constants are an important building block for constructing expressions, it is important to be able to write constant values for each of the basic data types."
s = "World"

# pprint(dir(string))

#  'capitalize',
print(string.capitalize())

#  'casefold',
print(string.casefold())

#  'lower',
print(string.lower())

#  'upper',
print(string.upper())

#  'title',
print(string.title())

#  'istitle',
print('The Byte Of Python'.istitle())

#  'isupper',
print('A'.isupper())

#  'islower',
print('a'.islower())

#  'swapcase', 用于对字符串的大小写字母进行转换
print("A of byte of Flask".swapcase())

#  'center',
print(s.center(20))

#  'rjust',
print(s.rjust(20))

#  'ljust',
print(s.ljust(20))

#  'zfill'
print(s.zfill(20))

#  'split',
lst = 'Life is short, Your need Python.'.split()
print(lst)

#  'join',
print(' '.join(lst))

#  'rsplit',
print('http://www.python.org'.rsplit(".", 1))

#  'splitlines',
print("Hello, Pick.\nLearning program of python\n".splitlines())

#  'strip',
print('  study of English    '.strip())

#  'rstrip',
print('  study of English    '.rstrip())

#  'lstrip',
print('  study of English    '.lstrip())

#  'startswith',
print('A simple example of flask'.startswith('A'))

#  'endswith',
print('A simple example of flask'.endswith('ask'))

#  'count',
print(string.count('a'))

#  'encode',
print(string.encode())

#  'format',
print('The {0} of {1}'.format('Example', 'Django'))

#  'format_map',
print("The {effect} of {name}".format_map({'effect': 'Example', 'name': 'Tornado'}))

#  'replace',
print('The Example of Django'.replace('Django', 'Flask'))

#  'index',
print(string.index('are'))

#  'rindex',
print(string.rindex('are'))

#  'expandtabs', 返回字符串中的 tab 符号('\t')转为空格后生成的新字符串
print('However, the inhibitive\teffect needs further study.'.expandtabs())

#  'find',
print('The effect of DM on bone DM metabolism'.find('DM'))

#  'rfind',
print('The effect of DM on bone DM metabolism'.rfind('DM'))

#  'partition',
print("www.python.org".partition("."))

#  'rpartition',
print("www.python.org".rpartition("."))

#  'maketrans' and 'translate', 根据参数table给出的表(包含 256 个字符)转换字符串的字符
table = str.maketrans("aeiou", "12345")
print("from string import maketrans".translate(table))

#  'isalnum', 是否字母或数字
print('we123'.isalnum())

#  'isalpha', 是否字母
print('we'.isalpha())

#  'isascii',

#  'isdecimal', 是否为十进制数
print("100".isdecimal())

#  'isdigit',  判断字符串是否是一个整型
print("0123".isdigit())

#  'isnumeric', 判断字符串是否是一个整型
print('23'.isnumeric())

#  'isidentifier', 判断是否是非法字符
print('\n'.isidentifier())

#  'isprintable', 是否为可打印字符

#  'isspace', 若是空格则为真
print(' '.isspace())

# Final output
print(string)
