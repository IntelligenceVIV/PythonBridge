# @Time    : 2019/4/18 3:10
# @Author  : Noah
# @File    : list_methods.py
# @Software: PyCharm
# @description: list methods
from faker import Faker
import pprint

fake = Faker()

lst = fake.pylist()

# use faker module generate new list
pprint.pprint(lst)

# 'append'
lst.append('faker data')

# 'clear'
lst.clear()

# 'copy'
l = lst.copy()
pprint.pprint(l)

# 'count'
n = lst.count('faker data')
print(n)

# 'extend'
lst.extend(['name', 'text', 'address'])

# 'index'
i = lst.index('name')
print(i)

# 'insert'
lst.insert(0, 'Hello World')

# 'pop'
lst.pop()  # remove last element

# 'remove'
lst.remove('Hello World')

# 'reverse'
lst.reverse()

# 'sort'
lst.sort()

# Final output
pprint.pprint(lst)
