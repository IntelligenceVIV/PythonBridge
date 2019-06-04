# @Time    : 2019/4/18 5:56
# @Author  : Noah
# @File    : function.py
# @Software: PyCharm
# @description: function effect
#################################################################################
# built-in function
lst = [12, 23, 17, 10, 19, 31]
m, n, l = max(lst), min(lst), len(lst)
print(m, n, l)

#################################################################################
# filter
def fun(x):
    return x > 5


l_filter = [i for i in filter(fun, range(10))]
print(l_filter)

#################################################################################
# reversed
l_reversed = [i for i in reversed(range(10))]
print(l_reversed)

#################################################################################
# sorted
l_sorted = sorted([12, 8, 5, 3, 11, 9, 10])
print(l_sorted)

#################################################################################
# enumerate
for k, v in enumerate(['name', 'address', 'text']):
    print(k, v)

#################################################################################
# zip
for k, v in zip(['a', 'b', 'c', 'd'], [11, 12, 13, 14]):
    print(k, v)

#################################################################################
# map
l_map = [i for i in map(lambda x: x ** 2, range(10))]
print(l_map)

#################################################################################
# reduce
from functools import reduce

sum_reduce = reduce(lambda x, y: x + y, range(10))
print(sum_reduce)


#################################################################################
# callable
def fun(x, y):
    return x + y
print(callable(fun))

#################################################################################
# generate formula => list dict set
l_generate = [i for i in range(10) if i % 2 == 1]
print(l_generate)

s_generate = {i for i in range(10) if i % 3 == 1}
print(s_generate)

d_generate = {k: v for k, v in zip([1, 2, 3], ['name', 'address', 'text'])}
print(d_generate)

#################################################################################
