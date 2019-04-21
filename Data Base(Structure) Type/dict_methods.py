# @Time    : 2019/4/18 3:39
# @Author  : Noah
# @File    : dict_methods.py
# @Software: PyCharm
# @description: dict methods
from faker import Faker
from pprint import pprint

fake = Faker()

d = fake.pydict()

# use faker module generate new dict
pprint(d)

# pprint(dir(d))

#  'clear',
d.clear()

#  'copy',
d_c = d.copy()
pprint("dict data: {0}".format(d_c))

#  'fromkeys',
d_f = d.fromkeys(d, 'New Data')
pprint("dict fromkeys: {0}".format(d_f))

#  'get',
value = d.get('wide')
pprint(value)

#  'items',
elements = d.items()
pprint(elements)

#  'keys',
keys = d.keys()
pprint(keys)

#  'values'
values = d.values()
pprint(values)

#  'pop',
d.pop('apply')

#  'popitem',
d.popitem()

#  'setdefault',
d.setdefault('phone', 'Apple')

#  'update',
d.update({'world': 'hello'})

# Final output
pprint(d)
