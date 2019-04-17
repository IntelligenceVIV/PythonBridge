# @Time    : 2019/4/18 3:31
# @Author  : Noah
# @File    : tuple_methods.py
# @Software: PyCharm
# @description: tuple methods
from faker import Faker
import pprint

fake = Faker()

t = fake.pytuple()

# use faker module generate new tuple
pprint.pprint(t)

# print(dir(t))

# 'count'
n = t.count('obqAh')
print(n)

# 'index'
i = t.index('obqAh')
print(i)
