# @Time    : 2019/4/18 3:40
# @Author  : Noah
# @File    : set_methods.py
# @Software: PyCharm
# @description: set methods
from faker import Faker
from pprint import pprint

fake = Faker()

s = fake.pyset()

# use faker module generate new list
pprint(s)

s1 = {1,3,4,5,6}
s2 = {3,4,1,8,9}

# pprint(dir(s))

#  'add',
s.add('address')

#  'clear',
s.clear()

#  'copy',
s_c = s.copy()
pprint(s_c)

#  'difference',
element = s1.difference(s2) # => s1 - s2
print("The operate result: ", element)

#  'difference_update',
s1.difference_update(s2) # => s1 = s1 - s2
print("The operate result: ", s1)

#  'discard',
s.discard("address")  #  区别是remove()方法移除一个不存在元素时会发生错误

#  'intersection',
elements = s1.intersection(s2) # => s1 & s2
print("The operate result: ", elements)

#  'intersection_update',
s1.intersection_update(s2) # => s1 = s1 & s2
print("The operate result: ", s1)

s3, s4 = {1, 2, 3}, {1, 2, 3, 4, 5, 6}
#  'isdisjoint', => 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False
print(s3.isdisjoint(s4))

#  'issubset',
print(s3.issubset(s4)) # s3 <= s4

#  'issuperset',
print(s3.issuperset(s4)) # s3 >= s4

#  'pop',
s.pop()

#  'remove',
s.remove('address')

#  'symmetric_difference',
element = s1.symmetric_difference(s2) # => s1 ^ s2
print("The operate result: ", element)

#  'symmetric_difference_update',
s1.symmetric_difference_update(s2) # => s1 = s1 ^ s2
print("The operate result: ", s1)

#  'union',
elements = s1.union(s2) # => s1 | s2
print("The operate result: ", elements)

#  'update'
s.update({1, 2, 3, 4, 5})

# Final output
pprint(s)